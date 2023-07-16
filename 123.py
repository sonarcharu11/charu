print("Select your Choice:")
print("1. For Loop")
print("2. While Loop")
choice = int( input() )
if( choice == 1 ):
 for x in range(1,8,2):
 print(x)
elif( choice == 2 ):
 count=1;
 while( count< 8):
 print(count)
 count+=2;
else:
 print( "Ok" )