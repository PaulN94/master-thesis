import json
import curses

class Menu:
    def __init__(self, data, path=[]):
        self.data = data
        self.selected_idx = 0
        self.selections = set()
        self.path = path

    def display_menu(self, stdscr):
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        
        for idx, item in enumerate(self.data):
            x = w//4
            y = h//4 + idx
            circle = '○' if idx not in self.selections else '●'
            
            display_str = f"{circle} {item}"
            
            if idx == self.selected_idx:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, display_str)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, display_str)
        
        # Display the possible navigation keys at the bottom
        instructions = "Arrow Keys: Navigate | Space: Select | Right: Expand | Enter: Save & Exit"
        stdscr.addstr(h-2, w//4, instructions)
        
        stdscr.refresh()

    def run(self, stdscr):
        while True:
            self.display_menu(stdscr)
            key = stdscr.getch()
            
            if key == curses.KEY_UP and self.selected_idx > 0:
                self.selected_idx -= 1
            elif key == curses.KEY_DOWN and self.selected_idx < len(self.data)-1:
                self.selected_idx += 1
            elif key == 32:  # Space bar
                if self.selected_idx in self.selections:
                    self.selections.remove(self.selected_idx)
                else:
                    self.selections.add(self.selected_idx)
            elif key == curses.KEY_RIGHT:
                next_path = self.path + [list(self.data.keys())[self.selected_idx]]
                next_menu = Menu(self.data[next_path[-1]], next_path)
                next_menu.run(stdscr)
            elif key == curses.KEY_ENTER or key in [10, 13]:
                break

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    with open("configuration.json", "r") as file:
        data = json.load(file)
    llms = data["data"]["llms"]

    menu = Menu(llms)
    menu.run(stdscr)

    for idx in menu.selections:
        selected_key = list(llms.keys())[idx]
        data["configuration"]["llm_evaluation"]["llms"][selected_key]["test"] = True

    with open("configuration_1.json", "w") as file:
        json.dump(data, file, indent=4)

# Run the program
curses.wrapper(main)
