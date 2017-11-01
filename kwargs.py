#**kwargs

def flower_colors(**kwargs):
  print(kwargs)

flower_colors(rose='red', violet='blue', daisy='white' )
flower_colors(1='red', 2='violet', 3='white')
#for some reason, you can't use integers as keywords when
#you use kwargs
#Chris says he really doesn't use **kwargs often
