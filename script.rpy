# The script of the game goes in this file.

# Declare characters used by this game.
define e = Character("Eileen")
define p = Character("[player_name]")
define m = Character("Mama")
define r = Character("Rose")
define A = Character("Developer Arwa")
define config.default_text_cps = 25

# Déclaration des images redimensionnées بأسماء جديدة ومضبوطة
image bg_sa9f = Transform("sa9f", xysize=(1920, 1080))
image bg_7amam = Transform("7amam", xysize=(1920, 1080))
image bg_kitchen = Transform("kitchen", xysize=(1920, 1080))
image bg_food = Transform("food-removebg-preview", xysize=(1920, 1080))
image bg_rout = Transform("rout", xysize=(1920, 1080))
image bg_sa7a = Transform("sa7a", xysize=(1920, 1080))
image bg_class = Transform("class", xysize=(1920, 1080))
image bg_contin = Transform("contin", xysize=(1920, 1080))
image bg_lunch = Transform("lunch-removebg-preview", xysize=(1920, 1080))
image bg_leave = Transform("leave", xysize=(1920, 1080))
image bg_spagiti = Transform("_sbagiti-removebg-preview", xysize=(1920, 1080))

# تصريح الشخصيات مع تكبير الحجم (Zoom / Transform) باش يبانو مزيان وما يجيوش صغار
image char_mama = Transform("happymama-removebg-preview", zoom=3)
image char_bizar = Transform("bizarmama", zoom=3)
image char_monster = Transform("manster-removebg-preview", zoom=4)
image char_mochawah = Transform("mochawah-removebg-preview", zoom=3)

# The game starts here.

label start:
    $ _preferences.text_cps = 40
    $ player_name = renpy.input("What is your name?", default="")
    $ player_name = player_name.strip()
    
    if player_name == "":
        $ player_name = "Meow"

    scene black

    # تشغيل الموسيقى الخلفية
    play music "audio/Tetuano - Abyss (freetouse.com).mp3"

    p "What is that sound?"
    menu:
        "Wake up":
            jump wak

        "Back to sleep":
            jump sleep

label sleep:
    scene bg_kitchen
    "I decided to close my eyes and sleep a bit more..."
    show char_mama
    m "Hey! Wake up, lazy head! It's the first day of school, you're going to be late!"
    p "Oh no, okay mama, I'm waking up now!"
    jump wak_after_sleep

label wak:      
    scene bg_sa9f
    m "Oh, is that the alarm?"
    m "Oh, the first day of school!"
    m "Oh yes, I will see my bestie."
    m "Finally!"
    scene bg_kitchen
    show char_mama
    m "Oh my god, you are awake on time, that's good! Now go to the toilet, wash your face, and brush your teeth."

label wak_after_sleep:
    p "Okay, mama."
    m "Good, and don't forget to wash your teeth."
    p "Don't worry, mama."
    m "Okay, finish and come to eat breakfast."
    p "Okay, mama."
    scene bg_7amam
    p "Let's see..."
    scene black 
    p "I'm finished, yes!"
    scene bg_7amam
    p "First I need to change my clothes."
    p "That's it, I did it."
    p "I changed it."
    p "Mama will be so happy and surprised."
    scene bg_kitchen
    show char_mama
    m "You finished, my little baby, good job!"
    show char_mama
    m "Oh, so you changed your clothes?"
    p "Yes, I know you're gonna love it."
    show char_mama
    m "Yes, my little baby, I'm so, so, so, so happy!"
    m "But now you need to eat this, your best..."
    m "Pancakes!"
    p "Yes, thanks, mommy, you are the best mom in the world!"
    m "Yes, my little [player_name], let's eat."
    p "Okay."
    scene bg_food
    "Why does the food look like that?"
    menu:
        "Ask mama":
            jump asckmama

        "Just eat":
            jump eat

label eat:
    scene bg_food
    "I decided to just eat it quietly without asking questions..."
    "It tastes really weird, but I finished it anyway."
    jump go_to_school

label asckmama:
    scene bg_food
    show char_bizar
    m "Mama, what is that?"
    m "That doesn't look like a pancake."
    p "This is a normal pancake."
    p "Just eat it, baby."
    p "Just eat, baby."
    "Why is mama so angry?"
    p "Eat, baby, eat."
    m "Okay, mama."
    scene bg_food
    "Oh, it tastes weird, but mama says it's normal."

label go_to_school:
    scene bg_kitchen
    show char_mama
    p "Oh, now it's time for school."
    m "Yes, mama."
    scene bg_rout
    "Oh, that is the school bus, I'm so excited!"
    p "This is the time to go to school, but don't forget to eat the lunch box."
    m "Don't worry, mama, I will eat it."
    p "Okay, good luck."
    m "Bye, mama."
    scene black
    "And just like that, I'm at school."
    scene bg_sa7a
    menu:
        "Talk to friend":
            jump talkeat

        "Don't talk with her":
            jump notalkeat

label notalkeat:
    scene bg_sa7a
    "I decided to stay quiet and go straight to class without talking to anyone."
    scene bg_class
    "The bell rang, and the classes started."
    jump school_end

label talkeat:                 
    scene bg_sa7a 
    p "Hi, Rose."
    r "Yo, my bestie!"
    r "I missed you so much, [player_name]."
    p "I missed you too, my Rose."
    p "I hope we are in the same class."
    r "Me too. So, what did you do in this vacation?"
    p "Nothing special, just..." 
    "But really, I don't know what I did." 
    r "Just what?"
    p "Ah, just normal."
    p "What about you, Rose?"
    r "Me? I went to the beach, I went to Disneyland, and I did everything I wanted!"
    p "That's good, I hope you feel good."
    r "Yes, thanks."
    p "Oh, here is the bell! Let's see what your class is."
    r "My class is 2."
    p "No, I'm in 1."
    r "Oh no, I want to be with you!"
    p "Me too, but now we need to go to class. See you in the lunch break."
    r "Okay, see you later."
    scene bg_class
    "This is the first day, looks like any normal day."

label school_end:
    "And just like that, the class ends."
    scene black 
    "Finally, I'm finished."
    scene bg_contin
    "This is the lunch time."
    scene bg_lunch
    p "Oh, why is lunch like that?"
    p "But mama said I need to eat all of it."
    p "What is this? I think it is meat."
    p "Oh, I love eating meat!"
    p "That's way good, but... it tastes a bit different."
    r "Hi, [player_name]."
    p "Hi, Rose."
    r "So, how do you feel on the first day?"
    p "It is normal."
    p "What about you?"
    r "Normal, like you."
    scene black
    "Like that, I finished the first day of school, and now I will see mama."
    scene bg_kitchen
    show char_bizar
    p "Hi, mama."
    m "Hi, my little boy."
    p "But mama, why are you like that? You're different."
    m "No, [player_name], I'm so normal. Did you eat your lunch?"
    p "Yes, mama, I ate the lunch, but the meat tasted different."
    m "Don't worry, [player_name], I'm just using different meat."
    p "Okay, mama."
    m "Take a shower and change your clothes."
    p "Okay, mama."
    m "I will cook the dinner."
    m "And don't enter the kitchen!"
    p "Okay, mama, don't worry."
    scene black 
    "I'm finished now, what should I do?"
    "I will help mama with the dinner."
    "Mama will be happy."
    "But mama said not to enter the kitchen."
    "Mama will be angry."
    menu:
        "Go to the kitchen":
            jump kitcheneat

        "Stay in living room":
            jump stayleaveat 

label kitcheneat:
    scene bg_kitchen
    "Oh, nothing here."
    "Oh, now what is that, mama?"
    scene bg_kitchen
    show char_monster
    p "Mama... is this mama?" 
    play sound "s1.mp3"
    m "Oh, my little baby! I said don't enter the kitchen."
    p "I'm sorry, mama, I just wanted to help you."
    play sound "2s.mp3"
    m "Okay, my little one, no problem."
    m "Sit here and watch me cooking."
    p "Okay, mama."
    "Is she cooking? Mama... this is not mama, but..."
    play sound "s4.mp3"
    m "Baby, what do you want to eat?"
    p "Nothing, mama, just anything."
    play sound "3s.mp3"
    m "Okay, what about eating spaghetti and meatballs?"
    p "Okay, mama."
    "I know this is not mama, but I'll stay a good kid."
    play sound "4s.mp3"
    m "Good baby, watch me cooking."
    p "Okay, mama."
    "The meat I ate today is... mama's meat!"
    scene bg_kitchen
    show char_monster
    m "I finished cooking, you need to eat it all."
    scene bg_kitchen
    show char_mochawah
    scene bg_spagiti
    p "Okay, mama."
    p "Thanks, mama, that's so delicious."
    play sound "s8.mp3"
    m "That's good. What about the meat?"
    p "It is good mama."
    play sound "s6.mp3"
    m "That's good, baby, now finish it."
    p "Okay, mama."
    m "Good boy, now go to sleep."
    p "Okay, mama."
    scene bg_kitchen
    "This is not mama, and now she doesn't look like mama anymore, but I still listen to her."
    scene black
    A "You finished the game! Thanks for playing my game."
    return

label stayleaveat:
    scene bg_leave
    "I will be a good boy and listen to mama."
    "Mama will be happy."
    show char_mama
    m "Oh, my little good boy."
    m "You listened to mama."
    show char_mochawah
    p "Mama..."
    "Why can't I sleep? Why is mama like that?" 
    "She looks like a monster!"
    "No... but mama is not a monster."
    show char_mama
    m "My little one, you must be hungry."
    "I can't talk, so I just shake my head to say yes."
    m "Oh, my little baby, I cooked for you some spaghetti."
    p "Yes, thank you, mama."
    scene bg_leave
    show char_monster
    show bg_spagiti
    "But... this is a mama's finger!"
    m "Eat, baby, my little one, eat, eat!"
    p "Okay, mama."
    p "I finished, mama."
    m "Good job, now go to sleep."
    p "Okay, mama."
    scene bg_kitchen
    p "Now I should sleep, mama will be mad if I stay awake at this time."
    scene black
    "End of the game, I hope you like it."
    return