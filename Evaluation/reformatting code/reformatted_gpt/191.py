def make_transparent(alpha=0.15, *args):
    """
    A function to make colors transparent.
    """
    if alpha < 0 or alpha > 1:
        raise ValueError("alpha must be between 0 and 1")
    alpha = int(255 * alpha)
    new_color = col2rgb(col=list(args), alpha=False)

    def make_transparent(col, alpha):
        return rgb(red=col[0], green=col[1], blue=col[2], alpha=alpha, maxColorValue=255)

    new_color = [make_transparent(col, alpha=alpha) for col in new_color]
    return new_color