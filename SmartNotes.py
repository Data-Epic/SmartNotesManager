from datetime import datetime


# Base class to represent a general note
class Note:
    note_id_counter = 1  # Static counter to assign unique IDs to each note

    def __init__(self, content):
        # the note with its content and assign it a unique ID
        self.id = Note.note_id_counter
        Note.note_id_counter += 1
        self.content = content
        self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def display(self):
        return f"[{self.id}] {self.created_at} - {self.content}"


# The subclass for text-based notes
class TextNote(Note):
    def display(self):
        # This will Override the display method to indicate it's a text note
        return f"Text Note {super().display()}"


# This subclass for reminder-based notes, inherits from the base Note class
class ReminderNote(Note):
    def __init__(self, content, reminder_time):
        super().__init__(content)
        self.reminder_time = reminder_time

    def display(self):
        # Overriding the display method to show the reminder time as well
        return f"Reminder Note {super().display()} (Reminder: {self.reminder_time})"


# Class to manage a collection of notes (adding, deleting, displaying, and searching)
class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note_type, content, reminder_time=None):
        # Adds a new note to the notes list based on the type specified (text or reminder)
        if note_type.lower() == "text":
            note = TextNote(content)
        elif note_type.lower() == "reminder" and reminder_time:
            note = ReminderNote(content, reminder_time)
        else:
            print("Invalid note type or missing reminder time.")
            return
        self.notes.append(note)
        print(f"Note added: {note.display()}")

    def delete_note(self, note_id):
        # Delete a note by its ID
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                print(f"Note {note_id} deleted.")
                return
        print("Note not found.")

    def show_notes(self):
        # Display all stored notes
        if not self.notes:
            print("No notes available.")
        else:
            for note in self.notes:
                print(note.display())

    def search_notes(self, keyword):
        # Search for notes containing a specific keyword
        results = [note for note in self.notes if keyword.lower() in note.content.lower()]
        if results:
            for note in results:
                print(note.display())
        else:
            print("No matching notes found.")


# Main program execution when the script is run directly
if __name__ == "__main__":
    my_notes = NotesManager()
    while True:
        print("\nOptions: add, delete, show, search, exit")
        choice = input("Choose an option: ").strip().lower()
        if choice == "add":
            note_type = input("Enter note type (text/reminder): ").strip().lower()
            content = input("Enter note content: ").strip()
            reminder_time = None
            if note_type == "reminder":
                reminder_time = input("Enter reminder time (YYYY-MM-DD HH:MM AM/PM): ").strip()
            my_notes.add_note(note_type, content, reminder_time)

        elif choice == "delete":
            note_id = int(input("Enter note ID to delete: "))
            my_notes.delete_note(note_id)

        elif choice == "show":
            my_notes.show_notes()

        elif choice == "search":
            keyword = input("Enter keyword to search: ").strip()
            my_notes.search_notes(keyword)

        elif choice == "exit":
            break

        else:
            print("Invalid option. Try again.")
