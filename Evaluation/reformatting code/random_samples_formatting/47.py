data, labels = vectorize_docs(
    artist="linkin-park",  # specify artist
    albums=["hybrid-theory"],  # specify album(s)
    keep_album=False,  # option to use the album name as a delimiter
    titlify=True,  # converts song title to original format
)

song_to_search = "Crawling"
for i, song in enumerate(labels):
    if song == song_to_search:
        display(Markdown("**Song name: **" + labels[i])) 
        display(Markdown("**Lyrics:**")) 
        print data[i][:1000] + "..."
        sample_lyrics = data[i]
        break