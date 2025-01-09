class BrowserHistoryManager:
    def __init__(self):
        self.back_stack = []  # Stack for back navigation
        self.forward_queue = []  # Queue for forward navigation
        self.current_page = None  # The current page being viewed

    # Visit a new URL
    def visit_url(self, url):
        if self.current_page:
            self.back_stack.append(self.current_page)  # Push current page to back stack
        self.current_page = url
        self.forward_queue.clear()  # Clear forward queue
        print(f"Visited: {url}")

    # Navigate back
    def back(self):
        if not self.back_stack:
            print("No previous page to go back to!")
        else:
            self.forward_queue.insert(0, self.current_page)  # Enqueue current page to forward queue
            self.current_page = self.back_stack.pop()  # Pop from back stack
            print(f"Moved back to: {self.current_page}")

    # Navigate forward
    def forward(self):
        if not self.forward_queue:
            print("No forward page to navigate to!")
        else:
            self.back_stack.append(self.current_page)  # Push current page to back stack
            self.current_page = self.forward_queue.pop(0)  # Dequeue from forward queue
            print(f"Moved forward to: {self.current_page}")

    # View current page
    def view_current_page(self):
        if self.current_page:
            print(f"Current page: {self.current_page}")
        else:
            print("No page is currently open!")

    # View back and forward history
    def view_history(self):
        print("\n--- Browser History ---")
        print("Back History:", self.back_stack if self.back_stack else "None")
        print("Forward History:", self.forward_queue if self.forward_queue else "None")
        print("-----------------------")

# Main program
def main():
    manager = BrowserHistoryManager()

    while True:
        print("\n=== Browser History Manager ===")
        print("1. Visit URL")
        print("2. Back")
        print("3. Forward")
        print("4. View Current Page")
        print("5. View History")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            url = input("Enter the URL: ")
            manager.visit_url(url)
        elif choice == "2":
            manager.back()
        elif choice == "3":
            manager.forward()
        elif choice == "4":
            manager.view_current_page()
        elif choice == "5":
            manager.view_history()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
