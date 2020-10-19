# polybar-quotation

This polybar module reads file with famous quotations and shows them on bar.
You can also truncate quotation.


## Functionality

- LMB - shows next line of quote.
- RMB - shows author.

## conf.json

- quotation_file - name of file with all quotes. (should be in data/ folder)
- active_record - name of file with currently visible quote. (should be in data/ folder)
- line_max_length - maximal count of characters that can be displayed at screen.
- separator - separates lines with given separator.
- left_quote, right_quote - chars that will be used as citation quotes. 
- alt_left_quote, alt_right_quote - chars that will wrap author's name.

## Instalation

- Clone repository ```sh
  git clone https://github.com/pikulo-kama/polybar-quotation
  ```
- ```sh
  mv -r polybar-quotation/ ~/.config/polybar/scripts/
  ```
- Add this line ```sh
  exec_always --no-startup-id $HOME/.config/polybar/scripts/polybar-quotation/quot.py --random
  ```
  
