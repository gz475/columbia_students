import sys

def dump_text( filename ):
    """ This will dump the txt of a file 
    to a large list

    """
    line_list = open( filename ).readlines()

    output_lines = []
    for line in line_list:
        output_lines.append( line.split() )

    return output_lines


def filter_text( filename, shape ):
    for line in dump_text( filename ):
        if line[4] == shape:
            print line


def max_duration( filename ):
    max_d = 0
    candidate = 0
    for line in dump_text( filename ):
        if line[5] != 'Duration':  
            candidate = int( line[5] )
        if candidate >= max_d: 
            max_d = candidate
    
    return max_d


if __name__ == "__main__":
    filter_text( sys.argv[1], sys.argv[2] )
    print max_duration( sys.argv[1] )
