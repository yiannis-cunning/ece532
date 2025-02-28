

input dx


sync @ hsync

pleft = 0
pright = 1

dest_left = 0
dest_right = dx

fixed_point sum = 0

for each input pixel:


    a = max(dest_left, pleft)
    b = min(dest_right, pright)

    f = (b - a)

    sum += f*v;

    if(dest_right == pright):
        increment both
    if(dest_right > pright):
        increment pixel
        pleft += 1
        pright += 1
    else:
        increment sum
        dest_left += dx
        dest_right += dx