# 📚 polybar-quotation

This polybar module reads file with famous quotations and shows them on bar.
You can also truncate quotation.


![](screenshots/single.gif)  
- *Single line quote*  

![](screenshots/multi.gif)  
- *Multi line quote*  

## Functionality

- LMB - shows next line of quote.
- RMB - shows author.

## Configuration

- **quotation_file** - name of file with all quotes. (should be in data/ folder)
- **active_record** - name of file with currently visible quote. (should be in data/ folder)
- **line_max_length** - maximal count of characters that can be displayed at screen.
- **separator** - separates lines with given separator.
- **left_quote, right_quote** - chars that will be used as citation quotes. 
- **alt_left_quote, alt_right_quote** - chars that will wrap author's name.

## Installation

- Clone repository
  ```sh
  git clone https://github.com/pikulo-kama/polybar-quotation
  ```
- Move files to polybar scripts
  ```sh
  mv -r polybar-quotation/ ~/.config/polybar/scripts/
  ```
- Add this line to ```~/.config/i3/config``` file
  ```sh
  exec_always --no-startup-id $HOME/.config/polybar/scripts/polybar-quotation/quot.py --random 
  ```
- Open ```hooks.sh``` and change bar name to yours
  ```sh
  bar_name="Your bar name"
  ```
 - Install fonts from ```fonts``` directory (Optional)
 
## Module

  ```ini
  [module/quotation]
  type = custom/ipc
  hook-0 = ~/.config/polybar/scripts/polybar-quotation/quot.py --current-line
  hook-1 = ~/.config/polybar/scripts/polybar-quotation/quot.py --author

  initial = 1

  click-left = ~/.config/polybar/scripts/polybar-quotation/hooks.sh 1
  click-right = ~/.config/polybar/scripts/polybar-quotation/hooks.sh 2

  format-font = 3
  format-prefix = "Y  "
  format-underline = #15b39b
  ```
  Make sure you have ipc enabled in your bar, if not add this line to ```[bar/name]``` section
  ```ini 
  enable-ipc = true
  ```
  
  If you installed fonts then add this line to your ```[bar/name]``` section
  ```ini 
  font-2 = "Iconic Pictograms Bold:size=11;4"
  ```
  
  **NOTE:** if you want to change quote just restart your i3wm (```$mod+shift+r```)
  
