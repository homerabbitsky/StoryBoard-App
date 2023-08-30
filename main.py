class Scene:

  def __init__(self, scene_number, location, description):
    self.scene_number = scene_number
    self.location = location
    self.description = description


class Storyboard:

  def __init__(self, title):
    self.title = title
    self.scenes = []

  def add_scene(self, scene):
    self.scenes.append(scene)

  def display(self):
    print(f"Storyboard: {self.title}\n")
    for scene in self.scenes:
      print(f"Scene {scene.scene_number}:")
      print(f"Location: {scene.location}")
      print(f"Description: {scene.description}")
      print("=" * 30)


def main():
  print("Film Storyboard Creator\n")
  title = input("Enter the title of the storyboard: ")
  storyboard = Storyboard(title)

  while True:
    print("\nAdd a new scene:")
    scene_number = int(input("Scene Number: "))
    location = input("Location: ")
    description = input("Description: ")

    scene = Scene(scene_number, location, description)
    storyboard.add_scene(scene)

    another_scene = input("Add another scene? (y/n): ")
    if another_scene.lower() != 'y':
      break

  print("\nFinal Storyboard:")
  storyboard.display()


if __name__ == "__main__":
  main()

# this app has been created in tandem with Chat-GPT 3.5
# OpenAI. (2023). ChatGPT (August 3 Version) [Large language model]. https://chat.openai.com

#the package below is Tkinter

import tkinter as tk
from tkinter import messagebox


class Scene:

  def __init__(self, scene_number, location, description):
    self.scene_number = scene_number
    self.location = location
    self.description = description


class Storyboard:

  def __init__(self, title):
    self.title = title
    self.scenes = []

  def add_scene(self, scene):
    self.scenes.append(scene)


class StoryboardApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Film Storyboard Creator")

    self.title_label = tk.Label(root,
                                text="Enter the title of the storyboard:")
    self.title_label.pack()

    self.title_entry = tk.Entry(root)
    self.title_entry.pack()

    self.add_scene_button = tk.Button(root,
                                      text="Add Scene",
                                      command=self.add_scene)
    self.add_scene_button.pack()

    self.finish_button = tk.Button(root,
                                   text="Finish Storyboard",
                                command=self.finish_storyboard)
    self.finish_button.pack()

    self.storyboard = Storyboard("")

  def add_scene(self):
    scene_number = len(self.storyboard.scenes) + 1
    location = input("Location: ")
    description = input("Description: ")

    scene = Scene(scene_number, location, description)
    self.storyboard.add_scene(scene)
    messagebox.showinfo("Scene Added",
                        f"Scene {scene_number} added to the storyboard.")

  def finish_storyboard(self):
    self.storyboard.title = self.title_entry.get()
    self.display_storyboard()

  def display_storyboard(self):
    display_text = f"Storyboard: {self.storyboard.title}\n\n"
    for scene in self.storyboard.scenes:
      display_text += f"Scene {scene.scene_number}:\n"
      display_text += f"Location: {scene.location}\n"
      display_text += f"Description: {scene.description}\n"
      display_text += "=" * 30 + "\n"

    self.display_label = tk.Label(root, text=display_text)
    self.display_label.pack()


root = tk.Tk()
app = StoryboardApp(root)
root.mainloop()

########### CTRL + / will un-comment and comment these out
