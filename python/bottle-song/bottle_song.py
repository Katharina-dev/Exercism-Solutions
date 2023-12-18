def recite(start, take=1):
    numbers = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    endings = {True: 's', False: ''}
    song = []
    for i in range(start, start-take, -1):
        song.append("")
        song.extend(2 * [f"{numbers[i].capitalize()} green bottle{endings[bool(i-1)]} hanging on the wall,"])
        song.append("And if one green bottle should accidentally fall,")
        song.append(f"There'll be {numbers[i-1]} green bottle{endings[bool(i-2)]} hanging on the wall.")
    return song[1:]

