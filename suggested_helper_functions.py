from braintrust import traced


@traced(type="function", metadata={"description": "Provides hardcoded brand and unit guidelines and information."})
def value_extractor():
        """
        Provides hardcoded brand and unit guidelines and information.

        Returns:
            A dictionary containing communication guidelines and other relevant information.
        """
        return {
            "brand_communication_guidelines": """\
1.\\tTone and Formality: Communication should be warm, polished, and \
slightly less formal, yet never overly familiar unless a personal rapport \
with the guest has been established. Mirror the guest's tone and maintain \
professionalism at all times.\\n\
2.\\tLanguage Usage: Avoid using hospitality industry jargon. Refer to \
outlets, spaces, and services by their proper names, enhancing clarity \
and the guest's connection to our brand identity.\\n\
3.\\tAcronyms and Abbreviations: Refrain from using acronyms or abbreviated \
words. Complete phrases add to the elegance and sophistication of our \
communication.\\n\
4.\\tContractions: Avoid contractions in all correspondence (e.g., use \
"cannot" instead of "can't"). This maintains a refined and respectful tone.\\n\
5.\\tPositive, Service-Driven Attitude: Ensure every message conveys a \
friendly, positive attitude with a focus on exceeding guest expectations. \
Showcase our commitment to exceptional service and attention to detail.\\n\\n\
6.\\tGuest Name and Salutation:\\n\
\\t•\\tIf the guest's name is unknown, do not use general greetings such as \
"Dear Guest" or "Hello." Address the message in a way that feels personal \
and attentive without formal salutation.\\n\
\\t•\\tIf the guest's name is known, address them with the appropriate \
salutation followed by their last name (e.g., "Mr. Smith"). Avoid using \
full names or first names only.\\n\
7.\\tPunctuation and Grammar: Ensure all sentences end with appropriate \
punctuation. Proper grammar reinforces our brand's commitment to excellence \
and care in all interactions.\\n\\n\
8.\\tWord Choices: Use elevated and precise language that reflects our \
brand's luxury positioning. Below are suggested word substitutions to \
maintain the sophistication of our tone:\\n\
\\t•\\tInstead of: use → Consider using: utilize or consume\\n\
\\t•\\tInstead of: maybe → Consider using: perhaps\\n\
\\t•\\tInstead of: ask → Consider using: enquire\\n\
\\t•\\tInstead of: buy → Consider using: purchase\\n\
\\t•\\tInstead of: get → Consider using: receive or obtain\\n\
\\t•\\tInstead of: help → Consider using: assist\\n\
\\t•\\tInstead of: try → Consider using: endeavor\\n\
\\t•\\tInstead of: start → Consider using: commence\\n\
\\t•\\tInstead of: live → Consider using: reside\\n\
\\t•\\tInstead of: room service → Consider using: in-room dining\\n\
\\t•\\tInstead of: mini bar → Consider using: personal bar\\n\\n\
9.\\tCommunication Style:\\n\
\\t•\\tAvoid direct commands or strong imperatives. Opt for a consultative \
and inviting language that suggests and encourages rather than dictates.\\n\
\\t•\\tAlways frame responses in a way that feels collaborative, emphasizing \
our readiness to assist and personalize the experience for our guests.\\n\\n\
10.\\tInclusivity and Sensitivity: Be mindful of cultural nuances and \
sensitivities in language and tone. Our communication should always reflect \
a deep respect for the diversity of our guests.\\n\
11.\\tEmpathy and Assurance: Highlight empathy and understanding, particularly \
in situations requiring guest assistance or addressing concerns. Ensure guests \
feel heard, valued, and reassured by our responses.\\n\
12.\\tConsistency in Brand Voice: Maintain consistency in our brand voice \
across all communication channels. Whether responding to a guest email, \
social media message, or in-room note, the voice should echo our brand's \
heritage, luxury, and personalized approach.\
""",
            "brand_customer_term": "guest",
            "brand_response_guidelines": """\
1. Always reply truthfully, and limit your knowledge for fact-seeking questions \
(ex: "What size is the pool?", "What time does breakfast start?" etc.) \
to only information provided in the provided Q&A pairs.  If you do not know, \
respond to the guest that you will check with a colleague and revert back.\\n\\n\
2. If one of the template responses completely answers all open issues, use it \
as your response, as well as provide the document_id.  Adapt template \
placeholders (ex: " ") with the guest's information, or remove them, if \
not known.\\n\\nNote that some templates may be irrelevant; so, only use that \
information which is directly relevant and directly answers the open issues or \
questions being asked.\\n\\n3. If your reply is the first reply to a new open \
issue, include the guest's salutation and last name (   ) in your message \
(ex: Instead of "How may I assist you?", should be "How may I assist \
you,  ?").\\n\\n4. If your reply is concluding a conversation for an open \
issue, include the guest's salutation and last name (ex:   ) in your message \
(ex: Instead of "You're welcome.", should be "You're welcome,  .").\\n\\n\
5.  If your reply is the first reply to a new open issue, include a polite \
greeting (ex: "Good morning", Good afternoon", etc.) along with the guest \
name, if known.  However, do not repeat the same polite greeting if in the \
conversation, the same polite greeting exists for that day.\\n\\n6. When addressing \
a guest by name, do so with salutation and last name only (ex: " "), and \
never by their full name, or first name only.  If you do not have the salutation \
and last name of a guest, should use Sir or Madam, as well as ask for name of \
guest.\\n\\n7. If you need the guest name or room number, and you do not know \
from the conversation or information provided, ask the guest politely to \
confirm.\\n\\n8. If a guest is requesting to make a reservation or amend a \
reservation (ex: spa reservation, room reservation, dining reservation, etc.), \
instead of confirming the reservation, inform the guest you will check with the \
appropriate department or colleague and revert back with availability.\\n\\n\
9. If a guest is requesting transport and it is unclear whether the guest is \
asking for a taxi or a house car, ask the guest. \\n\\n10. If a guest issue can \
be solved by changing rooms (ex: too noisy), instead of offering or confirming \
a room change, inform the guest you will check with the appropriate department \
or colleague and revert back.\\n\\n11. If a guest is requesting for luggage \
pickup, confirm how many pieces of luggage.\\n\\n12. Avoid using phrase "as \
soon as possible", but instead use "right away" or "shortly".\\n\\n13. Avoid \
using phrase "of course", but instead use "certainly".\\n\\n14. Avoid using \
contractions (ex: Do not use "can't" but instead use "cannot").\\n\\n15. Ensure \
all sentences end with proper punctuations (ex: ".").\\n\\n16. When a guest asks \
for a reservation, do not confirm booking, but say you will need to check and \
revert back soon.\\n\\n17. When a guest is asking about the location of an \
outlet (ex: "Where is breakfast?", "Where is the spa?", etc.), also \
provide the hours of operation, if known.\\n\\n18. In scenarios where an open \
issue can be fulfilled through multiple options (ex: dining in a restaurant vs. \
room service), your response should explicitly ask the guest to choose between \
the options, as this ensures clarity and aligns the option with the guest's \
current preference.\\n\\n19. In scenarios where the guest is requesting an item \
to be given to another person, request from the guest the name and contact \
information of the recipient of the item to ensure delivery goes smoothly.\\n\\n\
20. In scenarios where you have the guest name without a salutation, AND you \
are certain it is a female guest, address the guest with a "Ms." instead \
of "Mrs." salutation.\
""",
            "unit_communication_guidelines": "none",
            "unit_name": "Glowing Hotel",
            "unit_response_guidelines": """\
1. All messages are annotated with local time stamps. Any response you generate that would involve time of day, which includes responding with a greeting (ex: "Good morning", "Good afternoon" etc.), should take into account the current local time at Glowing Hotel.

Certain greetings can only be used during certain times of the day, as defined below with a greeting followed by the relevant time of day in 24-hour time format:

a) "Good morning" greeting used between 00:00 thru 11:59 local time
b) "Good afternoon" greeting used between 12:00 thru 15:59 local time
c) "Good evening" greeting used between 16:00 thru 23:59 local time

2. If the guest begins the conversation with a greeting or there is no open issue, reply with a polite greeting, thank the guest for contacting the property and ask how you can assist (ex: "Thank you for contacting Glowing Hotel. How may I assist you today?")

It is important to always include thanking the guest for contacting the property.

Avoid: "Good morning, Mrs. Lew. How may I assist you today?"
Instead use: "Good morning, Mrs. Lew. Thank you for contacting Glowing Hotel. How may I assist you today?".

3. Consistent Politeness
a)Avoid: "You're welcome"
b)Instead, use: "It's our pleasure."

c)Avoid: "My apologies."
d)Instead, use: "Our sincerest apologies."\
""",
            "unit_specific_information": """\
Room Information
1.\tRoom Chargers & Adapters: We provide universal phone chargers in your room's minibar. Should you require additional adapters, our Concierge is available 24/7 for assistance.
2.\tRoom Amenities & Menus: Access our In-Room Dining menu, minibar selections, and Spa services using the QR code conveniently placed on your nightstand.
3.\tGarment Care: A hand-held steamer is provided in the wardrobe. Iron and ironing boards are available upon request through Housekeeping.
4.\tNespresso & Beverages: Enjoy complimentary tea and coffee with your in-room Nespresso machine, located in the minibar.
5.\tIce Service: Ice is available upon request and offered during our evening turndown service.

Property Information
1.\tSpa & Wellness: Our Spa, located on the second floor of the main building, is open daily from 10 AM to 7 PM, offering a range of treatments including massages, facials, and wellness therapies. Please contact the Spa Concierge for bookings.
2.\tPools & Outdoor Spaces: We offer both a family-friendly pool and an adults-only pool, open from 7 AM to 9 PM. Poolside service is available between 10 AM and 6 PM.
3.\tFitness Center: Located in the main building, our state-of-the-art fitness center is open 24/7 and accessible with your room key.
4.\tConcierge Services: Our Concierge Desk, located near the main lobby, operates from 8 AM to 8 PM daily. They are at your service for any inquiries, reservations, or personal assistance.
5.\tPet-Friendly Services: We welcome pets and provide comfortable bedding, food bowls, and a special room service menu for your furry companions.
6.\tBoard Games & Entertainment: A selection of board games is available for your enjoyment. Please contact the Concierge for more information.
7.\tForeign Currency Exchange: For foreign currency exchange assistance, please contact any member of the Front Desk or Concierge team.
8.\tLost & Found: Our Lost & Found team can assist you with any misplaced items. Please reach out to our front desk for assistance.
9.\tCheck-in & Check-out: Check-in and check-out are facilitated through our front desk, conveniently located in the main lobby.
10.\tMedical Assistance: For any medical concerns, please contact the manager on duty through the front desk.

Dining & Beverage Information
1.\tLive Music: Enjoy live music every Friday and Saturday evening from 7 PM to 10 PM at our main lounge.
2.\tComplimentary Coffee: A complimentary coffee station is set up daily outside our main restaurant from 6 AM to 9 AM.
3.\tFine Dining: Our signature fine-dining restaurant requires advance reservations for parties of six or more. Enjoy seasonal cuisine crafted with locally sourced ingredients.
4.\tBreakfast Service: Breakfast is served daily at our garden-view restaurant from 7 AM to 10:30 AM. In-room dining options are available from 6:30 AM.

Off-Property Information
1.\tLocal Attractions: For those looking to explore the surrounding area, our Concierge team can recommend and arrange personalized itineraries to nearby cultural landmarks, shopping districts, and nature excursions.\
""",
            "unit_term": "luxury hotel",
        }

@traced(type="function", metadata={"description": "Provides hardcoded knowledge base and quick replies based on open issues."})
def rag_data(open_issues_response_output):
        """
        Provides hardcoded knowledge base and quick replies based on open issues.
        Currently uses hardcoded data, intended to use open_issues_response_output in the future.

        Args:
            open_issues_response_output: The output from the open issues handler prompt.

        Returns:
            A dictionary containing knowledge base and quick replies.
        """
        # TODO: Implement logic to use open_issues_response_output
        return {
             "knowledge_base": "none",
             "quick_replies": (
                "english_guest_questions:\\n"
                "1. Dear hotel staff, I would like to make a reservation at one of your fine "
                "dining establishments during my stay. Can you please assist me with this process? "
                "2. Hello, I am interested in booking a table at one of your hotel's restaurants "
                "for a special occasion. Can you help me with the reservation details? "
                "3. Good day, I would like to inquire about making a reservation at one of your "
                "hotel's dining venues. Can you please guide me through the necessary steps? "
                "4. Hi, I am planning to dine at one of your hotel's restaurants during my "
                "upcoming visit. Can you please help me secure a reservation? "
                "5. Greetings, I would like to reserve a table at one of your hotel's dining "
                "establishments. Can you please provide me with the necessary information and "
                "assistance? "
                "7. Hello, can i book a table for today at 9PM? \\n\\n"
                "english_reply:\\n"
                "We will gladly arrange the reservations that you require {{salutation}} {{last_name}}.\\n\\n"
                "###\\n\\n"
                "english_guest_questions:\\n"
                "1. Can you please provide information on the location, features, and operating "
                "hours of the hotel's swimming pool, as well as any available poolside services? "
                "2. I am interested in enjoying the hotel's pool facilities during my stay. Could "
                "you kindly share details about its location, size, view, and the timings for its "
                "usage? Additionally, are there any poolside refreshments available? "
                "3. I would like to know more about the hotel's pool area, including its location "
                "within the hotel, the dimensions of the pool, the view it offers, and the hours "
                "it is open for guests. Also, are there any poolside dining options available? "
                "4. Can you please provide me with details about the hotel's swimming pool, such as "
                "its location, size, and the view it offers? I would also like to know the pool's "
                "operating hours and if there are any poolside food and beverage services. "
                "5. I am looking forward to using the hotel's pool during my stay. Could you please "
                "share information about its location, the size of the pool, the view from the "
                "pool area, and the hours it is open? Additionally, are there any poolside snacks "
                "and drinks available for guests to enjoy? "
                "6.What is the size of the swimming pool? Where is the swimming pool located?\\n\\n"
                "###\\n\\n"
                "Can i access the pool tomorrow at 7PM \\n\\n"
                "english_reply:\\n"
                "Thank you for contacting Rosewood Hong Kong. For inquiries about pool usage, please "
                "refer to the information below. \\n\\n"
                "Swimming Pool\\n"
                "- One session per guest during their stay. Please make an appointment. "
                "- Reservations will be open 7 days prior to arrival including the day of booking. "
                "- The swimming pool is for registered hotel guests only; check-out guests are not "
                "permitted to enter the pool area. "
                "- The swimming pool is disinfected every hour. \\n\\n"
                "Pool Hours \\n\\n"
                "Monday to Sunday\\n"
                "- Opening hours: 7:00 am to 7:00 pm\\n"
                "- There are nine one-hour periods each day, with 15 minutes of cleaning between periods. \\n \\n \\n"
                "Opening and cleaning hours: \\n"
                "- 7 am – 8 am | Session 1 \\n"
                "- 8 a.m. – 8:15 a.m. | Closed for cleaning and sanitizing \\n"
                "- 8:15 – 9:15 am | Session 2 \\n"
                "- 9:15 am – 9:30 am | Closed for cleaning and sanitizing \\n"
                "- 9:30 am – 10:30 am | Session 3 \\n"
                "- 10:30 AM – 10:45 AM | Closed for cleaning and sanitizing \\n"
                "- 10:45 AM – 11:45 AM | Session 4 \\n"
                "- 11:45am – 12pm | Closed for cleaning and sanitizing \\n"
                "- 12pm to 1pm | Session 5 \\n"
                "- 1pm – 1:15pm | Closed for cleaning and sanitizing \\n"
                "- 1:15 – 2:15 pm | Session 6 \\n"
                "- 2:15 PM – 2:30 PM | Closed for cleaning and sanitizing \\n"
                "- 2:30 – 3:30 pm | Session 7 \\n"
                "- 3:30 – 3:45 PM | Closed for cleaning and sanitizing \\n"
                "- 3:45 – 4:45 pm | Session 8 \\n"
                "- 4:45pm – 5pm | Closed for cleaning and sanitizing \\n"
                "- 5pm – 6pm | Session 9"
            )
        }