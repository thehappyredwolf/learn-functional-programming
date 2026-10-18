def get_median_font_size(font_sizes: list[int]) -> int | None:
    if len(font_sizes) == 0:
        return None
    elif len(font_sizes) % 2 == 0:
       return sorted(font_sizes)[(len(font_sizes) // 2) - 1]
    return sorted(font_sizes)[len(font_sizes) // 2]
