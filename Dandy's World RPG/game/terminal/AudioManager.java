package terminal;

import javax.sound.sampled.*;
import java.io.*;

public class AudioManager {
    private SourceDataLine line;
    private Thread playThread;
    private volatile boolean shouldLoop = false;
    private volatile boolean isPlaying = false;

    private File getAssetsDir() {
        File dir = new File("game/assets");
        if (!dir.exists()) dir = new File("../assets");
        if (!dir.exists()) dir = new File("assets");
        return dir;
    }

    public void play(String fileName) {
        stop();
        File file = new File(getAssetsDir(), fileName);

        if (!file.exists()) {
            System.err.println("File not found: " + file.getAbsolutePath());
            return;
        }

        playThread = new Thread(() -> {
            isPlaying = true;
            do {
                streamAudio(file);
            } while (shouldLoop && isPlaying);
        });
        playThread.start();
    }

    private void streamAudio(File file) {
        try (AudioInputStream in = AudioSystem.getAudioInputStream(file)) {
            AudioFormat baseFormat = in.getFormat();
            AudioFormat targetFormat = new AudioFormat(
                AudioFormat.Encoding.PCM_SIGNED, 
                baseFormat.getSampleRate(), 16, 
                baseFormat.getChannels(), baseFormat.getChannels() * 2, 
                baseFormat.getSampleRate(), false // Little-endian
            );

            try (AudioInputStream decodedIn = AudioSystem.getAudioInputStream(targetFormat, in)) {
                DataLine.Info info = new DataLine.Info(SourceDataLine.class, targetFormat);
                
                line = null;
                for (Mixer.Info mixerInfo : AudioSystem.getMixerInfo()) {
                    Mixer mixer = AudioSystem.getMixer(mixerInfo);
                    if (mixer.isLineSupported(info)) {
                        line = (SourceDataLine) mixer.getLine(info);
                        break; 
                    }
                }

                if (line == null) {
                    throw new LineUnavailableException("No mixer supports this format. Check your OS sound settings.");
                }

                line.open(targetFormat);
                line.start();

                byte[] buffer = new byte[4096];
                int nBytesRead = 0;
                while (nBytesRead != -1 && isPlaying) {
                    nBytesRead = decodedIn.read(buffer, 0, buffer.length);
                    if (nBytesRead != -1) line.write(buffer, 0, nBytesRead);
                }
                
                line.drain();
                line.stop();
                line.close();
            }
        } catch (Exception e) {
            System.err.println("CRITICAL: " + e.getMessage());
        }
    }


    public void stop() {
        isPlaying = false;
        if (line != null) {
            line.stop();
            line.flush();
        }
    }

    public void setLooping(boolean loop) {
        this.shouldLoop = loop;
    }
}

