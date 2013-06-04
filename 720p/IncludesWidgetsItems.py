
# coding: utf-8

from collections import OrderedDict

prop = OrderedDict(

    RecommendedMovie = (
        'DBID', 'Title', 'OriginalTitle', 'Year', 'Genre', 'Studio', 'Country', 
        'Plot', 'PlotOutline', 'Tagline', 'Runtime', 'Rating', 'mpaa', 'Director', 
        'Trailer', 'Art(poster)', 'Art(fanart)', 'Art(clearlogo)', 'Art(clearart)', 
        'Art(landscape)', 'Art(banner)', 'Art(discart)', 'Resume', 'PercentPlayed', 
        'Watched', 'File', 'Play', 
        'VideoCodec', 'VideoResolution', 'VideoAspect', 'AudioCodec', 'AudioChannels',
    ),
        
    RecentMovie = (
        'DBID', 'Title', 'OriginalTitle', 'Year', 'Genre', 'Studio', 'Country', 
        'Plot', 'PlotOutline', 'Tagline', 'Runtime', 'Rating', 'mpaa', 'Director', 
        'Trailer', 'Art(poster)', 'Art(fanart)', 'Art(clearlogo)', 'Art(clearart)', 
        'Art(landscape)', 'Art(banner)', 'Art(discart)', 'Resume', 'PercentPlayed', 
        'Watched', 'File', 'Play', 
        'VideoCodec', 'VideoResolution', 'VideoAspect', 'AudioCodec', 'AudioChannels',
    ),
    
    RecommendedEpisode = (
        'DBID', 'Title', 'Episode', 'EpisodeNo', 'Season', 'Plot', 'TVshowTitle', 'Rating', 
        'Runtime', 'Premiered', 'Art(thumb)', 'Art(tvshow.fanart)', 'Art(tvshow.poster)', 
        'Art(tvshow.banner)', 'Art(tvshow.clearlogo)', 'Art(tvshow.clearart)', 'Art(tvshow.landscape)', 
        'Art(tvshow.characterart)', 'Art(season.poster)', 'Studio', 'mpaa', 'Resume', 'PercentPlayed',
         'Watched', 'File', 'Play', 'VideoCodec', 'VideoResolution', 'VideoAspect', 
         'AudioCodec', 'AudioChannels', 
    ),
    
    RecentEpisode = (
        'DBID', 'Title', 'Episode', 'EpisodeNo', 'Season', 'Plot', 'TVshowTitle', 'Rating', 
        'Runtime', 'Premiered', 'Art(thumb)', 'Art(tvshow.fanart)', 'Art(tvshow.poster)', 
        'Art(tvshow.banner)', 'Art(tvshow.clearlogo)', 'Art(tvshow.clearart)', 'Art(tvshow.landscape)', 
        'Art(tvshow.characterart)', 'Resume', 'PercentPlayed', 'Watched', 'File', 
        'Path', 'Play', 'VideoCodec', 'VideoResolution', 'VideoAspect', 'AudioCodec', 'AudioChannels', 
    ),
    
    RandomEpisode = (
        'DBID', 'Title', 'Episode', 'EpisodeNo', 'Season', 'Plot', 'TVshowTitle', 'Rating', 
        'Runtime', 'Premiered', 'Art(thumb)', 'Art(tvshow.fanart)', 'Art(tvshow.poster)', 
        'Art(tvshow.banner)', 'Art(tvshow.clearlogo)', 'Art(tvshow.clearart)', 'Art(tvshow.landscape)', 
        'Art(tvshow.characterart)', 'Resume', 'PercentPlayed', 'Watched', 'File', 
        'Path', 'Play', 'VideoCodec', 'VideoResolution', 'VideoAspect', 'AudioCodec', 'AudioChannels', 
    ),
    
    RecommendedMusicVideo = (
        'DBID', 'Title', 'Artist', 'Year', 'Plot', 'Genre', 'Runtime', 'Thumb', 'Fanart', 'Art(thumb)', 
        'Art(fanart)', 'File', 'Path', 'Resume', 'PercentPlayed', 'Watched', 'Play', 'VideoCodec', 
        'VideoResolution', 'VideoAspect', 'AudioCodec', 'AudioChannels', 
    ),
    
    RecentMusicVideo = (
        'DBID', 'Title', 'Artist', 'Year', 'Plot', 'Genre', 'Runtime', 'Thumb', 'Fanart', 'Art(thumb)', 
        'Art(fanart)', 'File', 'Path', 'Resume', 'PercentPlayed', 'Watched', 'Play', 'VideoCodec', 
        'VideoResolution', 'VideoAspect', 'AudioCodec', 'AudioChannels', 
    ),
    
    RecommendedAlbum = (
        'Title', 'Label', 'Artist', 'Genre', 'Theme', 'Mood', 'Style', 'Type', 'Year', 'RecordLabel', 
        'Description', 'Rating', 'Thumb', 'Fanart', 'Art(thumb)', 'Art(fanart)', 'Play',         
    ),
    
    RecentAlbum = (
        'Title', 'Label', 'Artist', 'Genre', 'Theme', 'Mood', 'Style', 'Type', 'Year', 'RecordLabel', 
        'Description', 'Rating', 'Thumb', 'Fanart', 'Art(thumb)', 'Art(fanart)', 'Play',         
    ),
    
    RandomArtist = (
        'Title', 'Genre', 'Thumb', 'Fanart', 'Art(thumb)', 'Art(fanart)', 'Description', 'Born', 
        'Died', 'Formed', 'Disbanded', 'YearsActive', 'Style', 'Mood', 'Instrument', 'LibraryPath',         
    ),
    
    RandomSong = (
        'Title', 'Artist', 'Year', 'Rating', 'Album', 'Thumb', 'Fanart', 'Art(thumb)', 'Art(fanart)', 
        'File', 'Path', 'Play', 
    ),
    
    RandomAddon = (
        'Title', 'Author', 'Summary', 'Version', 'Path', 'Thumb', 'Fanart', 'Art(thumb)', 'Art(fanart)', 
        'Type',
    )     
)


def main():
    LIMIT = 20
    print '<includes>'
    for (category, propnames) in prop.items():
        print '\t<include name="Widget%sItems">' % category
        print '\t\t<content>'
        for i in range(1,LIMIT+1):
                #<label>$INFO[Window(Home).Property(RecommendedMovie.1.Title)]</label>
				#<label2>$INFO[Window(Home).Property(RecommendedMovie.1.Year)]</label2>
				#<icon>$INFO[Window(Home).Property(RecommendedMovie.1.Art(poster))]</icon>
				#<thumb>$INFO[Window(Home).Property(RecommendedMovie.1.Art(fanart))]</thumb>
            print '\t\t\t<item id="%d">' % i
            print '\t\t\t\t<label>$INFO[Window(Home).Property(%s.%d.Title)]</label>' % (category, i)
            
            if 'Episode' in category:
                print '\t\t\t\t<label2>$INFO[Window(Home).Property(%s.%d.Season),$LOCALIZE[31087] , • ]$INFO[Window(Home).Property(%s.%d.Episode),$LOCALIZE[31088] ]</label2>' % (category, i, category, i)
                print '\t\t\t\t<property name="Fanart">$INFO[Window(Home).Property(%s.%d.Art(tvshow.fanart))]</property>' % (category, i)
            else:
                print '\t\t\t\t<property name="Fanart">$INFO[Window(Home).Property(%s.%d.Art(fanart))]</property>' % (category, i)
            
            if 'Movie' in category:
                print '\t\t\t\t<label2>$INFO[Window(Home).Property(%s.%d.Runtime)]</label2>' % (category, i)
                
            if 'Album' in category:
                print '\t\t\t\t<label2>$INFO[Window(Home).Property(%s.%d.Artist)]</label2>' % (category, i)
                
            if 'Addon' in category:
                print '\t\t\t\t<label2>$INFO[Window(Home).Property(%s.%d.Author)]</label2>' % (category, i)
                
            print '\t\t\t\t<icon>$INFO[Window(Home).Property(%s.%d.Art(fanart))]</icon>' % (category, i)
            print '\t\t\t\t<thumb>$INFO[Window(Home).Property(%s.%d.Art(thumb))]</thumb>' % (category, i)
            for propname in propnames:
                print '\t\t\t\t<property name="%s">$INFO[Window(Home).Property(%s.%d.%s)]</property>' % (propname, category, i, propname)
                if 'Episode' in category and 'Art(tvshow.' in propname:
                    tvshowless_name = propname.replace('tvshow.','')
                    print '\t\t\t\t<property name="%s">$INFO[Window(Home).Property(%s.%d.%s)]</property>' % (tvshowless_name, category, i, propname)
            print '\t\t\t\t<onclick>$INFO[Window(Home).Property(%s.%d.Play)]</onclick>' % (category, i)
            print '\t\t\t\t<visible>!IsEmpty(Window(Home).Property(%s.%d.Title))</visible>' % (category, i)
            print '\t\t\t</item>'
        print '\t\t</content>'
        print '\t</include>'
    print '</includes>'
        


main()


            
