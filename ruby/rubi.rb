require 'pnglitch'
PNGlitch.open('C:\Users\lukas\Downloads\image.png') do |p|
  p.change_all_filters 2
  p.each_scanline do |l|
    l.register_filter_encoder do |data, prev|
      data.size.times.reverse_each do |i|
        x = data.getbyte(i)
        v = prev ? prev.getbyte(i) : 0
        data.setbyte(i, (x - v) & 0xfe)
      end
      data
    end
  end
  p.output 'C:\Users\lukas\Downloads\image3.png'
end

require 'pnglitch'
PNGlitch.open('C:\Users\lukas\Downloads\image.png') do |p|
  p.each_scanline do |l|
    l.register_filter_encoder do |data, prev|
      data.size.times.reverse_each do |i|
        x = data.getbyte(i)
        v = prev ? prev.getbyte(i - 1) : 0
        data.setbyte(i, (x - v) & 0xff)
      end
      data
    end
  end
  p.output 'C:\Users\lukas\Downloads\image4.png'
end
(none|sub|up|average|paeth).