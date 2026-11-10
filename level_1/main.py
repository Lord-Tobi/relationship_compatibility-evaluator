def main():
    parameter_weights = {
        "Honesty": 15,
        "Loyalty": 15,
        "Communication": 10,
        "Shared values": 10,
        "Long-term commitment": 10,
        "Purpose": 10,
        "Financial responsibility": 10,
        "Emotional maturity": 10,
        "Trustworthiness": 10
    }
    parameter_total = 0
    for t in parameter_weights.values():
        parameter_total += t
    if parameter_total == 100:
        print("Parameter weights are valid.")
    else:
        print("Error: Parameter weights must total 100%.")
        return
    questions = {
        "Honesty": [
        {
        "question": "You accidentally receive more money than you should after making a purchase. What would you do?",
        "options": {
            "A": "Keep the money.",
            "B": "Keep it unless the person notices.",
            "C": "Return it if I realise the mistake.",
            "D": "Immediately inform the person and return the excess."
        }
        },
        {
        "question": "You make a mistake that negatively affects someone close to you. What would you do?",
        "options": {
            "A": "Deny responsibility.",
            "B": "Avoid discussing it.",
            "C": "Admit it if confronted.",
            "D": "Voluntarily admit the mistake and take responsibility."
        }
        },
        {
        "question": "You make a promise but later realise you cannot fulfil it. What would you do?",
        "options": {
            "A": "Pretend I never made the promise.",
            "B": "Make excuses when the person asks.",
            "C": "Explain when the person brings it up.",
            "D": "Communicate early, explain the situation and take responsibility."
        }
        }
        ],
        "Loyalty": [
        {
        "question": "At a gathering with friends, someone makes negative comments about your partner in their absence. What would you do?",
        "options": {
            "A": "Join in and make negative comments too.",
            "B": "Remain silent because I don't want to offend my friends.",
            "C": "Disagree but avoid getting involved in an argument.",
            "D": "Respectfully defend my partner and address the issue if necessary."
        }
        },
        {
        "question": "In a committed relationship, someone attractive expresses romantic interest. How do you handle it?",
        "options": {
            "A": "Explore the possibility secretly.",
            "B": "Enjoy the attention and continue entertaining the person.",
            "C": "Make clear I'm in a relationship but maintain some unnecessary flirtatious interaction.",
            "D": "Establish clear boundaries and avoid encouraging romantic interest."
        }
        },
        {
        "question": "Your partner shares something deeply personal with you. What do you do?",
        "options": {
            "A": "Share it with friends for something interesting to discuss.",
            "B": "Share it with someone else without considering my partner's comfort.",
            "C": "Keep it private but seek advice from someone trustworthy if necessary.",
            "D": "Respect their confidence and seek permission before sharing, except where safety requires appropriate intervention."
        }
        }
        ],
        "Communication": [
        {
        "question": "Your partner does something that genuinely upsets you. What do you do?",
        "options": {
            "A": "Keep quiet but become distant.",
            "B": "Express frustration through insults or hostility.",
            "C": "Wait until calm, then explain what upset me.",
            "D": "Communicate my feelings clearly, respectfully and directly."
        }
        },
        {
        "question": "Your partner explains something important but you strongly disagree. What do you do?",
        "options": {
            "A": "Interrupt and insist my position is correct.",
            "B": "Listen impatiently while preparing my response.",
            "C": "Allow them to finish, then explain my disagreement.",
            "D": "Listen attentively, ask questions and respectfully communicate my perspective."
        }
        },
        {
        "question": "Your partner wants to discuss an uncomfortable relationship issue. What do you do?",
        "options": {
            "A": "Avoid the conversation entirely.",
            "B": "Dismiss the issue because I don't consider it important.",
            "C": "Agree to discuss but struggle to engage openly.",
            "D": "Make time and work toward understanding and resolving the issue."
        }
        }
        ],
        "Financial responsibility": [
        {
        "question": "You receive monthly income. How do you manage it?",
        "options": {
            "A": "Spend freely without considering future obligations.",
            "B": "Pay immediate expenses but rarely plan beyond them.",
            "C": "Budget expenses and try to save consistently.",
            "D": "Budget, save, plan future obligations and make deliberate financial decisions."
        }
        },
        {
        "question": "You borrow money but experience unexpected financial difficulties before repayment. What do you do?",
        "options": {
            "A": "Ignore the debt and hope the person forgets.",
            "B": "Avoid the person because I cannot repay immediately.",
            "C": "Explain the situation when the person requests repayment.",
            "D": "Communicate proactively and propose a realistic repayment arrangement."
        }
        },
        {
        "question": "Your partner wants to discuss financial planning for the future. How do you respond?",
        "options": {
            "A": "I don't believe partners should discuss finances.",
            "B": "Discuss money only when financial problems arise.",
            "C": "Discuss goals but prefer to manage everything independently.",
            "D": "Discuss goals, responsibilities and plans while maintaining healthy financial boundaries."
        }
        }
        ],
        "Shared values": [
        {
        "question": "Doing what is morally right could cost you a personal advantage. What do you do?",
        "options": {
            "A": "Choose personal advantage regardless of the consequences.",
            "B": "Do what benefits me if nobody finds out.",
            "C": "Consider the consequences carefully before deciding.",
            "D": "Prioritise my principles even if it requires personal sacrifice."
        }
        },
        {
        "question": "Your partner values family involvement in your future. How do you approach this?",
        "options": {
            "A": "Completely reject family involvement.",
            "B": "Tolerate it but avoid making an effort.",
            "C": "Respect family relationships with reasonable boundaries.",
            "D": "Make a genuine effort to build healthy family relationships while maintaining appropriate boundaries."
        }
        },
        {
        "question": "Your partner takes Christian faith seriously and wants your future relationship to reflect those beliefs. How do you approach this?",
        "options": {
            "A": "Disregard his beliefs and expect him to abandon them.",
            "B": "Tolerate his beliefs but show no interest in understanding them.",
            "C": "Respect his beliefs even where differences exist.",
            "D": "Genuinely share and practise compatible Christian values in the relationship."
        }
        }
        ],
        "Long-term commitment": [
        {
        "question": "Your relationship goes through a difficult period involving disagreements and stress. What do you do?",
        "options": {
            "A": "Immediately consider ending the relationship.",
            "B": "Withdraw emotionally and wait for things to improve.",
            "C": "Try to work through difficulties, provided both are willing.",
            "D": "Work toward resolving issues through communication, mutual effort and appropriate support."
        }
        },
        {
        "question": "Your partner wants to discuss where the relationship is heading over the next five years. How do you respond?",
        "options": {
            "A": "Avoid discussing the future.",
            "B": "Give vague answers just to satisfy the conversation.",
            "C": "Discuss expectations but remain uncertain about specific plans.",
            "D": "Honestly discuss intentions, expectations and possible future plans."
        }
        },
        {
        "question": "You and your partner decide to build a family together. How do you view responsibilities?",
        "options": {
            "A": "Expect my partner to handle most responsibilities.",
            "B": "Participate only when convenient.",
            "C": "Believe responsibilities should be shared, though we may need to negotiate how.",
            "D": "Take responsibility, make sacrifices when necessary and work together toward shared goals."
        }
        }
        ],
        "Purpose": [
        {
        "question": "Where do you see yourself in the next five to ten years?",
        "options": {
            "A": "I have no interest in thinking about my future.",
            "B": "I have some wishes but rarely think about achieving them.",
            "C": "I have personal goals and some ideas about pursuing them.",
            "D": "I have clear goals and actively work toward them while remaining open to change."
        }
        },
        {
        "question": "Your partner has an important personal goal that requires time and effort. How do you approach it?",
        "options": {
            "A": "Expect him to abandon the goal to focus entirely on the relationship.",
            "B": "Tolerate the goal but show little interest in supporting it.",
            "C": "Encourage him while maintaining my own priorities.",
            "D": "Actively support his goal while pursuing my own aspirations."
        }
        },
        {
        "question": "You enter a serious relationship and discuss the kind of life you both want. What matters most?",
        "options": {
            "A": "Focus only on what I personally want.",
            "B": "Expect the relationship itself to determine my direction in life.",
            "C": "Consider both individual goals and possible shared goals.",
            "D": "Work toward a meaningful shared vision while respecting individual aspirations."
        }
        }
        ],
        "Emotional maturity": [
        {
        "question": "Your partner does something that makes you very angry. How do you respond?",
        "options": {
            "A": "React immediately regardless of what I say or do.",
            "B": "Become hostile, withdraw or give silent treatment.",
            "C": "Take time to calm down before discussing the issue.",
            "D": "Recognise my emotions, regulate my reaction and communicate respectfully."
        }
        },
        {
        "question": "Someone points out a genuine mistake in your behaviour. How do you respond?",
        "options": {
            "A": "Reject the criticism and blame the other person.",
            "B": "Become defensive and refuse to discuss it.",
            "C": "Consider the criticism even if accepting it is difficult.",
            "D": "Listen openly, acknowledge my shortcomings and make an effort to improve."
        }
        },
        {
        "question": "Something important doesn't go according to your expectations. How do you handle it?",
        "options": {
            "A": "Allow my frustration to affect everyone around me.",
            "B": "Blame others and struggle to move forward.",
            "C": "Accept the disappointment and try to find a way forward.",
            "D": "Process my emotions constructively, learn from the experience and adjust my expectations."
        }
        }
        ],
        "Trustworthiness": [
        {
        "question": "You make an important promise to your partner. How do you approach it?",
        "options": {
            "A": "Make promises without much concern about keeping them.",
            "B": "Try to keep promises but disregard them when inconvenient.",
            "C": "Take promises seriously and make an effort to fulfil them.",
            "D": "Make realistic commitments and communicate honestly if circumstances prevent fulfilment."
        }
        },
        {
        "question": "Your partner spends time with female colleagues or friends. How do you approach this?",
        "options": {
            "A": "Assume something inappropriate is happening without evidence.",
            "B": "Frequently question him and monitor his interactions.",
            "C": "Trust him but communicate when something genuinely makes me uncomfortable.",
            "D": "Give him reasonable trust and independence while maintaining open communication and mutually agreed boundaries."
        }
        },
        {
        "question": "Your partner is going through a difficult period and needs your support. How do you respond?",
        "options": {
            "A": "Disappear or avoid him because his problems are inconvenient.",
            "B": "Offer support only when convenient.",
            "C": "Make a genuine effort to support him within my abilities.",
            "D": "Be dependable, communicate honestly about what I can offer and follow through."
        }
        }
        ]
    }
    answer_scores = {
        "A": 0,
        "B": 3,
        "C": 7,
        "D": 10
    }
    for parameter in questions:
        if parameter not in parameter_weights:
            print(f"Error: {parameter} has no corresponding weight.")
            return
    for parameter in questions:
        if len(questions[parameter]) != 3:
            print(f"Error: {parameter} must have exactly 3 questions.")
            return
        for question in questions[parameter]:
            if len(question["options"]) != 4:
                print(f"Error: {parameter} must have four options per question.")
                return
            if question["options"].keys() != answer_scores.keys():
                print(f"Error: {parameter} has incorrectly labelled options.")
                return
    for parameter in parameter_weights:
        if parameter not in questions:
            print(f"Error: No questions defined for {parameter}.")
            return

    scores = {}
    answers = {}
    parameter_averages = {}
    weighted_contributions = {}
    final_score = 0.0
    weighted_contribution_total = 0
    eligible = False
    while True:
        faith = input("Are you a Christian? (YES/NO): ").strip().upper()

        if faith == "YES":
            eligible = True
            # Allow access
            break

        elif faith == "NO":
            # Display rejection message
            print("Thank you, maybe next time.")
            break

        else:
            print("Enter a valid choice from the options above.")
    if eligible:
        for parameter in questions:
            answers[parameter] = []
            scores[parameter] = []
            parameter_averages[parameter] = 0
            for question in questions[parameter]:
                print(question["question"])
        
                for option in question["options"]:
                    print(option,question["options"][option])
                option_choice = input("Enter options: ").strip().upper()
                while option_choice not in question["options"]:
                    print("Invalid choice. Please enter A, B, C or D.")
                    option_choice = input("Enter your choice: ").strip().upper()
                answers[parameter].append(option_choice)
                score = answer_scores[option_choice]
                scores[parameter].append(score)
        for parameter in scores:
            score_total = 0
            for score in scores[parameter]:
                score_total += score
        
            average = score_total / len(scores[parameter])
            parameter_averages[parameter] = average
        for parameter in parameter_averages:
            weighted_contribution = (parameter_averages[parameter] / 10) * parameter_weights[parameter]
    
            weighted_contributions[parameter] = weighted_contribution
    
        for c in weighted_contributions.values():
            weighted_contribution_total += c

        print("\n----- PARAMETER RESULTS -----")       
        final_score = round(weighted_contribution_total,2) 
        print(f"Final score: {final_score:.2f}%")


        for parameter,average in parameter_averages.items():
    
            print(f"{parameter}: {average:.2f}/10")
    
            contribution = weighted_contributions[parameter]
            print(f"Weighted contribution: {contribution:.2f}%")
            print()

        if 90 <= final_score <= 100:
            print("\nVery strong alignment")
        elif 80 <= final_score < 90:
            print("\nStrong alignment")
        elif 70 <= final_score < 80:
            print("\nGood alignment")
        elif 60 <= final_score < 70:
            print("\nModerate alignment")
        elif 50 <= final_score < 60:
            print("\nLimited alignment")
        else:
            print("\nLow alignment")
        print("\nNote: Results are based on self-reported answers.")
        print("\nThey do not objectively measure character or guarantee relationship success.")
        print("\nCommitment does not mean tolerating abuse or unhealthy treatment.")
    else:
        print("\nThank you for participating.")
    





main()