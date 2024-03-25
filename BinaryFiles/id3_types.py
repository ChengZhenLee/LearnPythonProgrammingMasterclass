id3_field_encodings = ['iso-8859-1', 'utf_16', 'utf_16_be', 'utf_8']

apic_picture_types = {0x00: 'Other',
                      0x01: '32x32_pixels_png_file_icon',
                      0x02: 'Other_file_icon',
                      0x03: 'Front_cover',
                      0x04: 'Back_cover',
                      0x05: 'Leaflet_page',
                      0x06: 'Media_(eg_label_side_of_CD)',
                      0x07: 'Lead_artist',
                      0x08: 'Artist',
                      0x09: 'Conductor',
                      0x0A: 'Band',
                      0x0B: 'Composer',
                      0x0C: 'Lyricist',
                      0x0D: 'Recording_Location',
                      0x0E: 'During_recording',
                      0x0F: 'During_performance',
                      0x10: 'Video_screen_capture',
                      0x11: 'A_bright_coloured_fish',
                      0x12: 'Illustration',
                      0x13: 'Band_logotype',
                      0x14: 'Publisher_logotype',
                      }

# Frame types, taken from https://id3.org/id3v2.3.0 and https://id3.org/id3v2.4.0-frames
frame_types = {
    b'AENC': 'Audio encryption',
    b'APIC': 'Attached picture',
    b'ASPI': 'Audio seek point index',
    b'COMM': 'Comments',
    b'COMR': 'Commercial frame',
    b'ENCR': 'Encryption method registration',
    b'EQU2': 'Equalisation',
    b'EQUA': 'Equalization',
    b'ETCO': 'Event timing codes',
    b'GEOB': 'General encapsulated object',
    b'GRID': 'Group identification registration',
    b'IPLS': 'Involved people list',
    b'LINK': 'Linked information',
    b'MCDI': 'Music CD identifier',
    b'MLLT': 'MPEG location lookup table',
    b'OWNE': 'Ownership frame',
    b'PRIV': 'Private frame',
    b'PCNT': 'Play counter',
    b'POPM': 'Popularimeter',
    b'POSS': 'Position synchronisation frame',
    b'RBUF': 'Recommended buffer size',
    b'RVA2': 'Relative volume adjustment',
    b'RVAD': 'Relative volume adjustment',
    b'RVRB': 'Reverb',
    b'SEEK': 'Seek frame',
    b'SIGN': 'Signature frame',
    b'SYLT': 'Synchronized lyric/text',
    b'SYTC': 'Synchronized tempo codes',
    b'TALB': 'Album/Movie/Show title',
    b'TBPM': 'BPM (beats per minute)',
    b'TCOM': 'Composer',
    b'TCON': 'Content type',
    b'TCOP': 'Copyright message',
    b'TDAT': 'Date',
    b'TDEN': 'Encoding time',
    b'TDLY': 'Playlist delay',
    b'TDOR': 'Original release time',
    b'TDRC': 'Recording time',
    b'TDRL': 'Release time',
    b'TDTG': 'Tagging time',
    b'TENC': 'Encoded by',
    b'TEXT': 'Lyricist/Text writer',
    b'TFLT': 'File type',
    b'TIME': 'Time',
    b'TIPL': 'Involved people list',
    b'TIT1': 'Content group description',
    b'TIT2': 'Title/songname/content description',
    b'TIT3': 'Subtitle/Description refinement',
    b'TKEY': 'Initial key',
    b'TLAN': 'Language(s)',
    b'TLEN': 'Length',
    b'TMCL': 'Musician credits list',
    b'TMED': 'Media type',
    b'TMOO': 'Mood',
    b'TOAL': 'Original album/movie/show title',
    b'TOFN': 'Original filename',
    b'TOLY': 'Original lyricist(s)/text writer(s)',
    b'TOPE': 'Original artist(s)/performer(s)',
    b'TORY': 'Original release year',
    b'TOWN': 'File owner/licensee',
    b'TPE1': 'Lead performer(s)/Soloist(s)',
    b'TPE2': 'Band/orchestra/accompaniment',
    b'TPE3': 'Conductor/performer refinement',
    b'TPE4': 'Interpreted, remixed, or otherwise modified by',
    b'TPOS': 'Part of a set',
    b'TPUB': 'Publisher',
    b'TRCK': 'Track number/Position in set',
    b'TRDA': 'Recording dates',
    b'TRSN': 'Internet radio station name',
    b'TRSO': 'Internet radio station owner',
    b'TSIZ': 'Size',
    b'TSOA': 'Album sort order',
    b'TSOP': 'Performer sort order',
    b'TSOT': 'Title sort order',
    b'TSRC': 'ISRC (international standard recording code)',
    b'TSSE': 'Software/Hardware and settings used for encoding',
    b'TSST': 'Set subtitle',
    b'TYER': 'Year',
    b'TXXX': 'User defined text information frame',
    b'UFID': 'Unique file identifier',
    b'USER': 'Terms of use',
    b'USLT': 'Unsychronized lyric/text transcription',
    b'WCOM': 'Commercial information',
    b'WCOP': 'Copyright/Legal information',
    b'WOAF': 'Official audio file webpage',
    b'WOAR': 'Official artist/performer webpage',
    b'WOAS': 'Official audio source webpage',
    b'WORS': 'Official internet radio station homepage',
    b'WPAY': 'Payment',
    b'WPUB': 'Publishers official webpage',
    b'WXXX': 'User defined URL link frame',
}
