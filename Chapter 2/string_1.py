# ---------------------------------------------------------------------------------
# Method 1
trial = "reversal"
new_trial = trial[::-1]

print(new_trial)

"""
Js equivalent: 
let trial = 'reversal';
let newTrial = trial.split('').reverse().join('');

console.log(newTrial);
"""


# ---------------------------------------------------------------------------------
# Method 2
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]


print(string_reverse("dinasour"))

"""
Js equivalent: 
function stringReverse(str) {
    if (str.length === 0) {
        return str;
    } else {
        return stringReverse(str.substring(1)) + str.charAt(0);
    }
}

console.log(stringReverse('dinosaur'));
"""


# ---------------------------------------------------------------------------------
# Method 3
def reverse_string_reversed(s):
    return "".join(reversed(s))


s = "Hello, World!"
reversed_s = reverse_string_reversed(s)
print(reversed_s)  # Output: !dlroW ,olleH


# ---------------------------------------------------------------------------------
# Method 4
def reverse_string_loop(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s


print(reverse_string_loop("hello kitty"))

"""
Js equivalent: 
function reverseStringLoop(s) {
    let reversedS = '';
    for (let i = s.length - 1; i >= 0; i--) {
        reversedS += s[i];
    }
    return reversedS;
}

console.log(reverseStringLoop('example'));  // Output: elpmaxe
"""
