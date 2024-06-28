import tkinter as tk
import pyshorteners
root=tk.Tk()
root.title("URL Shortener")
root.geometry("300x150")
# def shorten():
#     shortener=pyshorteners.Shortener()
#     short_url=shortener.tinyurl.short(longURL_entry.get())
#     print(shortURl_entry.insert(0,short_url))
def shorten():
    try:
        long_url = longURL_entry.get()
        if long_url:
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(long_url)
            shortURl_entry.delete(0, tk.END)
            shortURl_entry.insert(0, short_url)
        else:
            shortURl_entry.delete(0, tk.END)
            shortURl_entry.insert(0, "Enter a valid URL")
    except pyshorteners.exceptions.ShorteningErrorException as e:
        shortURl_entry.delete(0, tk.END)
        shortURl_entry.insert(0, "Error shortening URL")
    except Exception as e:
        shortURl_entry.delete(0, tk.END)
        shortURl_entry.insert(0, f"Error: {str(e)}")

longURl=tk.Label(root,text="Enter Long URL")
longURL_entry=tk.Entry(root)
shortURl=tk.Label(root,text="Output shortened URL")
shortURl_entry=tk.Entry(root)
shorten_button=tk.Button(root,text="Shorten URL",command=shorten)

longURl.pack()
longURL_entry.pack()
shortURl.pack()
shortURl_entry.pack()
shorten_button.pack()
root.mainloop()