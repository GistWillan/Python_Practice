import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("400x300")

        self.playlist = []
        self.current_track = 0

        self.create_widgets()
        pygame.init()

    def create_widgets(self):
        # 创建GUI部件
        self.label = tk.Label(self.master, text="Music Player", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, selectbackground="yellow", selectforeground="black")
        self.listbox.pack(pady=10)

        self.add_button = tk.Button(self.master, text="Add Song", command=self.add_song)
        self.add_button.pack(pady=10)

        self.play_button = tk.Button(self.master, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)

        self.next_button = tk.Button(self.master, text="Next", command=self.next_song)
        self.next_button.pack(pady=10)

    def add_song(self):
        # 添加歌曲到播放列表
        file_path = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)
            self.listbox.insert(tk.END, os.path.basename(file_path))

    def play_music(self):
        # 播放音乐
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()

    def stop_music(self):
        # 停止音乐
        pygame.mixer.music.stop()

    def next_song(self):
        # 播放下一首歌曲
        if self.playlist:
            self.current_track = (self.current_track + 1) % len(self.playlist)
            self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
