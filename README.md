# Browser History Manager Using Stack and Queue

## Problem Statement
Navigating a browser efficiently requires maintaining a proper history of visited pages. Users often need to navigate back to a previously visited page or forward to a page they just left. Managing this navigation history effectively is crucial for a smooth browsing experience.

## Description of the Project
The *Browser History Manager Using Stack and Queue* is a Python-based application that simulates the behavior of browser navigation. It utilizes two fundamental data structures:

1. *Stack*: To handle the back navigation history (LIFO - Last In, First Out).
2. *Queue*: To manage the forward navigation history (FIFO - First In, First Out).

This application enables users to:
- Visit new URLs and add them to the history.
- Navigate back to previously visited pages.
- Navigate forward to pages from the forward history.
- View the current page.
- View the entire navigation history (back and forward).

The program features a menu-driven interface for user interaction.

## Solution
### Key Features
1. *Visit URL*: Opens a new URL and clears the forward history.
2. *Navigate Back*: Moves the current page to the forward queue and loads the last visited page from the back stack.
3. *Navigate Forward*: Moves the current page to the back stack and loads the next page from the forward queue.
4. *View Current Page*: Displays the URL of the currently active page.
5. *View History*: Lists all pages in the back stack and forward queue.
6. *Exit*: Ends the application.

### Data Structures Used
- *Stack*: Efficiently manages back navigation history, allowing quick access to the last visited page.
- *Queue*: Handles forward navigation, enabling sequential movement to future pages.

### Implementation
The application uses Python lists to mimic the behavior of stacks and queues. The menu-driven interface ensures easy navigation and usability for users.

## Conclusion
The *Browser History Manager Using Stack and Queue* effectively demonstrates how data structures can be applied to manage browser navigation. It provides a structured and intuitive approach to handling back and forward navigation. This project is an excellent way to understand the real-world applications of stacks and queues while building a practical tool for managing browser history.
