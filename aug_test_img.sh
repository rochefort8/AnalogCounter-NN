#!/bin/bash

max=5
base=$1

# contrast
convert $base".png" -contrast $base"_cm_0".png
for ((i=0; i < $max; i++)); do
    let d=$i+1
    convert $base"_cm_"$i".png" -contrast $base"_cm_"$d".png"
done

# contrast
convert $base".png" -contrast $base"_cp_0".png
for ((i=0; i < $max; i++)); do
    let d=$i+1
    convert $base"_cp_"$i".png" -contrast $base"_cp_"$d".png"    
done

# blur

# blur
convert $base".png" -contrast $base"_b0_0".png
for ((i=0; i < $max; i++)); do
    let d=$i+1
    convert $base"_b0_"$i".png" -blur 2 $base"_b0_"$d".png"    
done

# gamma
convert $base".png" -contrast $base"_g0_0".png
for ((i=0; i < $max; i++)); do
    let d=$i+1
    convert $base"_g0_"$i".png" -gamma 0.95 $base"_g0_"$d".png"    
done
