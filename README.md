# 📅 are-we-together (in the same lecture?) 🎶

<img src="https://raw.githubusercontent.com/UP2014372/are-we-together/master/preview.gif">

## About <a name = "about"></a>

With the start of the new academic year, I have finally been able to attend physical lectures for the first time ever. On our course we are surprisingly not all together in the same lectures (despite there being 7 of us). 

This combined with the fact that some of us have our lectures before others makes talking about current work slightly confusing. 

This inspired me to find a way of working out who is in the same lectures, hence `are-we-together`.

## Getting Started <a name = "getting_started"></a>

### Prerequisites

All requirements are able to be installed via the `requirements.txt` file as shown below:
```bash
pip install -r requirements.txt
```

If you want to understand the structure of the DataFrame then have a look at [`development.ipynb`](https://github.com/UP2014372/are-we-together/blob/master/development.ipynb).

## Usage 
```python
usage: arewetogether.py [-h] (-f FILE [FILE ...] | -p PATH) [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE [FILE ...], --file FILE [FILE ...]
                        File names to be used
  -p PATH, --path PATH  Path to directory containing calendar files
  -o OUTPUT, --output OUTPUT
                        File to output to (destructive), omit to copy to clipboard
```


After running the script all output will be copied to your clipboard, simply paste as desired. 

If you are pasting into Discord then I would recommend [this plugin](https://betterdiscord.app/plugin/SplitLargeMessages). 
All it does is split a message that exceeds the character limit into multiple messages, to be used with [BetterDiscord](https://betterdiscord.app).
