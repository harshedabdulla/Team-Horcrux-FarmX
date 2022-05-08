def check_health(a):
    if a == 2 :
        return "Healthy"  #green
    elif a == 3:
        return "Low Moisture" #orange
    elif a== 1 :
        return "Not Healthy"  #red

def sec_color(b) :
    if b == 2 :
        return "hsl(147, 52%, 40%,0.5)"
    elif b == 3:
        return "hsl(23, 67%, 47%,0.5)"
    elif b == 1 :
        return "hsl(0, 97%, 67%,0.5)"

def sec_shadow(b) : 
    if b == 3 :
        return "0 0 20px hsl(23, 67%, 47%,0.9)"
    elif b == 2 :
        return "0 0 20px hsl(147, 52%, 40%,0.9)"
    elif b==1 :
        return "0 0 20px hsl(0, 97%, 67%,0.9)"