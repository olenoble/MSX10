################################################################################################################
################################################################################################################
# Very basic toolkit to generate spritedata.asm and spriteinfo.asm
import numpy

if __name__ == '__main__':
    filename = './graphics/sprites.c'

    ################################################################################################################
    ################################################################################################################
    # All variables
    background = '0x00000000'
    sprite_height = 16
    sprite_length = 16
    scaling = numpy.array([2 ** (sprite_length / 2-x-1) for x in range(int(sprite_length / 2))])

    ################################################################################################################
    ################################################################################################################
    # Load file
    with open(filename, 'rb') as f:
        txt = f.read()

    # Get the sprite data (ignore header)
    rawdata = txt.decode('utf8').split('] = {')[1]

    # Loop over each sprite    
    spriteiter = 1
    reachend = False
    remaining = rawdata
    output = []
    output_raw = []
    
    while not reachend:
        try:
            pos = remaining.index('{\n')
        except Exception as exc:
            pos = -1
            reachend = True

        if pos >= 0:
            # Get sprite
            print('Getting Sprite #%i' % spriteiter)
            origsprite = remaining[(pos + 2):]
            endorig = origsprite.index('}')
            origsprite = origsprite[:endorig]
            
            # Extract remaining
            remaining = remaining[(pos + 2 + endorig + 1):]

            # Now read the data properly and map it to ASM type data
            data_orig = origsprite.split('\n')[:-1]
            data_left = []
            data_right = []
            for i in range(sprite_height):
                row_data = [1 * (x != background) for x in data_orig[i].split(', ')[:sprite_length]]
                row_left = row_data[:int(sprite_length/2)]
                row_right = row_data[int(sprite_length/2):]
                data_left += [str(int((scaling * row_left).sum()))]
                data_right += [str(int((scaling * row_right).sum()))]
            
            output += [[','.join(data_left + data_right)]]
            output_raw += [data_left + data_right]
            spriteiter += 1
            
    # print(output)

    # combine
    sprite_to_combine = [0]
    combined_sprites = []
    for i in range(sprite_height * (sprite_length // 8)):
        for j in sprite_to_combine:
            combined_sprites += [output_raw[j][i]]
    
    combined_string = ','.join(combined_sprites)
    print('DATA ' + combined_string)
   

    # # write file
    # output += data_ending % maxsprite
    # with open('spritedata.asm', 'w') as f:
    #     f.write(output)

    # output_info += info_ending % maxsprite
    # with open('spriteinfo.asm', 'w') as f:
    #     f.write(output_info)

    print('Done ')

