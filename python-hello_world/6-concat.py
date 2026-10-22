cd /set-high_level_programming/python-hello_world

# 1. Write 6-concat.py using explicit string concatenation instead of an f-string
cat << 'EOF' > 6-concat.py
#!/usr/bin/python3
str1 = "Elmwood"
str2 = "Institute"

print("Welcome to " + str1 + " " + str2 + "!")
EOF

# 2. Make it executable and verify line count (must output 5)
chmod +x 6-concat.py
wc -l 6-concat.py
