print "\n".join(
    textfilter.normalize_text(
        sample_lyrics,
        sentences=True  # preserves sentences
    )
)