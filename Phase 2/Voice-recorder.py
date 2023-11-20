import sys
import sounddevice as sd
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import numpy as np
import wavio

class VoiceRecorder(QWidget):
    def __init__(self):
        super().__init__()

        self.filename = "recorded_audio.wav"
        self.duration = 5
        self.sample_rate = 44100
        self.recording = False

        self.init_ui()

    def init_ui(self):
        self.record_button = QPushButton("Record", self)
        self.record_button.clicked.connect(self.toggle_record)

        self.pause_button = QPushButton("Pause", self)
        self.pause_button.clicked.connect(self.pause_audio)
        self.pause_button.setEnabled(False)

        self.play_button = QPushButton("Play", self)
        self.play_button.clicked.connect(self.play_audio)
        self.play_button.setEnabled(False)

        self.status_label = QLabel("Status: Ready", self)

        layout = QVBoxLayout()
        layout.addWidget(self.record_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.play_button)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Voice Recorder')

    def toggle_record(self):
        if not self.recording:
            self.record_button.setText("Stop")
            self.pause_button.setEnabled(True)
            self.play_button.setEnabled(False)
            self.status_label.setText("Status: Recording...")

            # Record audio
            self.audio_data = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=2, dtype=np.int16)
            self.recording = True
        else:
            self.record_button.setText("Record")
            self.pause_button.setEnabled(False)
            self.play_button.setEnabled(True)
            self.status_label.setText("Status: Recording complete.")

            # Save audio to WAV file
            wavio.write(self.filename, self.audio_data, self.sample_rate, sampwidth=3)

            self.recording = False

    def pause_audio(self):
        sd.stop()
        self.record_button.setText("Record")
        self.pause_button.setEnabled(False)
        self.play_button.setEnabled(True)
        self.status_label.setText("Status: Recording paused.")

    def play_audio(self):
        self.status_label.setText("Status: Playing...")
        sd.play(self.audio_data, self.sample_rate)
        sd.wait()
        self.status_label.setText("Status: Playback complete.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    recorder = VoiceRecorder()
    recorder.show()
    sys.exit(app.exec_())
