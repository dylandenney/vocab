import datetime
import random

# A simple dictionary of words with their definitions and example sentences
vocabulary = {
    "serendipity": {
        "definition": "the occurrence and development of events by chance in a happy or beneficial way",
        "sentence": "A fortunate stroke of serendipity brought them together."
    },
    "pulchritudinous": {
        "definition": "physically beautiful; comely",
        "sentence": "She possessed a pulchritudinous appearance that captivated everyone."
    },
    "quintessential": {
        "definition": "representing the most perfect or typical example of a quality or class",
        "sentence": "He was the quintessential tough guy—strong, silent, and self-contained."
    },
    "acumen": {
        "definition": "the ability to make good judgments and quick decisions, typically in a particular domain",
        "sentence": "Her political acumen won her a place in the government."
    },
    "benevolent": {
        "definition": "Well-meaning and kindly.",
        "sentence": "A benevolent smile."
    },
    "amiable": {
        "definition": "Having or displaying a friendly and pleasant manner.",
        "sentence": "An amiable, unassuming fellow."
    },
    "venerate": {
        "definition": "Regard with great respect; revere.",
        "sentence": "Mother Teresa is venerated as a saint."
    },
    "prudent": {
        "definition": "Acting with or showing care and thought for the future.",
        "sentence": "No prudent money manager would authorize a loan without first knowing its purpose."
    },
    "languid": {
        "definition": "Displaying or having a disinclination for physical exertion or effort; slow and relaxed.",
        "sentence": "They turned with languid movements from back to front so as to tan evenly."
    },
    "indigenous": {
        "definition": "Originating or occurring naturally in a particular place; native.",
        "sentence": "The indigenous peoples of Siberia."
    },
    "harangue": {
        "definition": "A lengthy and aggressive speech.",
        "sentence": "They were subjected to a ten-minute harangue by two border guards."
    },
    "garner": {
        "definition": "Gather or collect (something, especially information or approval).",
        "sentence": "The police struggled to garner sufficient evidence."
    },
    "fervent": {
        "definition": "Having or displaying a passionate intensity.",
        "sentence": "A fervent supporter of the revolution."
    },
    "eloquence": {
        "definition": "Fluent or persuasive speaking or writing.",
        "sentence": "A preacher of great power and eloquence."
    },
    "deft": {
        "definition": "Neatly skillful and quick in one's movements.",
        "sentence": "A deft piece of footwork."
    },
    "candid": {
        "definition": "Truthful and straightforward; frank.",
        "sentence": "His responses were remarkably candid."
    },
    "brevity": {
        "definition": "Concise and exact use of words in writing or speech.",
        "sentence": "The report is notable for its brevity."
    },
    "arduous": {
        "definition": "Involving or requiring strenuous effort; difficult and tiring.",
        "sentence": "An arduous journey."
    },
    "affable": {
        "definition": "Friendly, good-natured, or easy to talk to.",
        "sentence": "An affable and agreeable companion."
    },
    "verbose": {
        "definition": "Using or expressed in more words than are needed.",
        "sentence": "Much academic language is obscure and verbose."
    },
    "tenacious": {
        "definition": "Tending to keep a firm hold of something; clinging or adhering closely.",
        "sentence": "A tenacious grip."
    },
    "resilient": {
        "definition": "Able to withstand or recover quickly from difficult conditions.",
        "sentence": "Babies are generally far more resilient than new parents realize."
    },
    "philanthropic": {
        "definition": "Seeking to promote the welfare of others, especially by donating money to good causes.",
        "sentence": "She is notable for her philanthropic work."
    },
    "nostalgia": {
        "definition": "A sentimental longing or wistful affection for a period in the past.",
        "sentence": "I was overcome with acute nostalgia for my days in college."
    },
    "juxtapose": {
        "definition": "Place or deal with close together for contrasting effect.",
        "sentence": "Black-and-white photos of slums were starkly juxtaposed with color images."
    },
    "innuendo": {
        "definition": "An allusive or oblique remark or hint, typically a suggestive or disparaging one.",
        "sentence": "A constant stream of innuendo, rumors, and outright lies."
    },
    "gregarious": {
        "definition": "Fond of company; sociable.",
        "sentence": "He was a popular and gregarious man."
    },
    "fortitude": {
        "definition": "Courage in pain or adversity.",
        "sentence": "She endured her illness with great fortitude."
    },
    "empathy": {
        "definition": "The ability to understand and share the feelings of another.",
        "sentence": "She'd shown empathy with others."
    },
    "dauntless": {
        "definition": "Showing fearlessness and determination.",
        "sentence": "Dauntless bravery."
    },
    "capricious": {
        "definition": "Given to sudden and unaccountable changes of mood or behavior.",
        "sentence": "A capricious and often brutal administration."
    },
    "benevolence": {
        "definition": "The quality of being well meaning; kindness.",
        "sentence": "He thanked them for their benevolence and support."
    },
    "xenophobia": {
        "definition": "Dislike of or prejudice against people from other countries.",
        "sentence": "The resurgence of racism and xenophobia."
    },
    "wistful": {
        "definition": "Having or showing a feeling of vague or regretful longing.",
        "sentence": "A wistful smile."
    },
    "ubiquitous": {
        "definition": "Present, appearing, or found everywhere.",
        "sentence": "His ubiquitous influence was felt by all the family."
    },
    "stoic": {
        "definition": "A person who can endure pain or hardship without showing their feelings or complaining.",
        "sentence": "He was stoic in the face of adversity."
    },
    "quell": {
        "definition": "Put an end to (a rebellion or other disorder), typically by the use of force.",
        "sentence": "Extra police were called to quell the disturbance."
    },
    "pensive": {
        "definition": "Engaged in, involving, or reflecting deep or serious thought.",
        "sentence": "A pensive mood."
    },
    "obstinate": {
        "definition": "Stubbornly refusing to change one's opinion or chosen course of action, despite attempts to persuade one to do so.",
        "sentence": "Her obstinate determination to pursue a career in radio."
    },
    "nuance": {
        "definition": "A subtle difference in or shade of meaning, expression, or sound.",
        "sentence": "The nuances of facial expression and body language."
    },
    "meticulous": {
        "definition": "Showing great attention to detail; very careful and precise.",
        "sentence": "The designs are hand-glazed with meticulous care."
    },
    "kindle": {
        "definition": "Light or set on fire; arouse or inspire (an emotion or feeling).",
        "sentence": "A love of art was kindled in me."
    },
    "jovial": {
        "definition": "Cheerful and friendly.",
        "sentence": "She was in a jovial mood."
    },
    "innate": {
        "definition": "Inborn; natural.",
        "sentence": "Her innate capacity for organization."
    },

}


vocabulary.update({
    "vivacious": {
        "definition": "Attractively lively and animated (especially of a woman).",
        "sentence": "She was vivacious and witty."
    },
    "tranquil": {
        "definition": "Free from disturbance; calm.",
        "sentence": "Her tranquil gaze."
    },
    "sublime": {
        "definition": "Of such excellence, grandeur, or beauty as to inspire great admiration or awe.",
        "sentence": "Mozart's sublime piano concertos."
    },
    "quixotic": {
        "definition": "Exceedingly idealistic; unrealistic and impractical.",
        "sentence": "A vast and perhaps quixotic project."
    },
    "omnipotent": {
        "definition": "Having unlimited power; able to do anything.",
        "sentence": "An omnipotent deity."
    },
    "nostalgic": {
        "definition": "Characterized by or exhibiting feelings of nostalgia (a sentimental longing or wistful affection for the past).",
        "sentence": "I felt a nostalgic pang."
    },
    "lament": {
        "definition": "A passionate expression of grief or sorrow.",
        "sentence": "His mother's night-long laments for his father."
    },
    "ingenious": {
        "definition": "(Of a person) clever, original, and inventive.",
        "sentence": "He was ingenious enough to overcome the limited budget."
    },
    "harbinger": {
        "definition": "A person or thing that announces or signals the approach of another.",
        "sentence": "Witch hazels are the harbingers of spring."
    },
    "gratuitous": {
        "definition": "Uncalled for; lacking good reason; unwarranted.",
        "sentence": "Gratuitous violence."
    },
    "enigma": {
        "definition": "A person or thing that is mysterious, puzzling, or difficult to understand.",
        "sentence": "Madeleine was still an enigma to him."
    },
    "dubious": {
        "definition": "Hesitating or doubting.",
        "sentence": "I was dubious about the whole idea."
    },
    "cryptic": {
        "definition": "Having a meaning that is mysterious or obscure.",
        "sentence": "He found his boss's instructions cryptic."
    },
    "bucolic": {
        "definition": "Relating to the pleasant aspects of the countryside and country life.",
        "sentence": "The church is lovely for its bucolic setting."
    },
    "astute": {
        "definition": "Having or showing an ability to accurately assess situations or people and turn this to one's advantage.",
        "sentence": "An astute businessman."
    },
    "anomaly": {
        "definition": "Something that deviates from what is standard, normal, or expected.",
        "sentence": "There are a number of anomalies in the present system."
    },
    "zenith": {
        "definition": "The time at which something is most powerful or successful.",
        "sentence": "In 1977, punk reached its zenith."
    },
    "yoke": {
        "definition": "A wooden crosspiece that is fastened over the necks of two animals and attached to the plow or cart that they are to pull.",
        "sentence": "A pair of oxen were yoked together by a wooden crosspiece."
    },
    "veracity": {
        "definition": "Conformity to facts; accuracy.",
        "sentence": "Officials expressed doubts concerning the veracity of the story."
    },
    "unfathomable": {
        "definition": "Incapable of being fully explored or understood.",
        "sentence": "His unfathomable reaction."
    },
    "trepidation": {
        "definition": "A feeling of fear or agitation about something that may happen.",
        "sentence": "The men set off in fear and trepidation."
    },
    "surreptitious": {
        "definition": "Kept secret, especially because it would not be approved of.",
        "sentence": "They carried on a surreptitious affair."
    },
    "reticent": {
        "definition": "Not revealing one's thoughts or feelings readily.",
        "sentence": "She was extremely reticent about her personal affairs."
    },
    "quandary": {
        "definition": "A state of perplexity or uncertainty over what to do in a difficult situation.",
        "sentence": "Kate was in a quandary."
    },
    "prolific": {
        "definition": "(Of a plant, animal, or person) producing much fruit or foliage or many offspring.",
        "sentence": "In captivity, tigers are prolific breeders."
    },
    "opulent": {
        "definition": "Ostentatiously rich and luxurious or lavish.",
        "sentence": "The opulent comfort of a limousine."
    },
    "neophyte": {
        "definition": "A person who is new to a subject, skill, or belief.",
        "sentence": "Four-day cooking classes are offered to neophytes and experts."
    },
    "myriad": {
        "definition": "A countless or extremely great number of people or things.",
        "sentence": "Myriads of insects danced around the light."
    },
    "kinetic": {
        "definition": "Relating to or resulting from motion.",
        "sentence": "The kinetic energy of an object is the energy it possesses due to its motion."
    },
    "jocular": {
        "definition": "Fond of or characterized by joking; humorous or playful.",
        "sentence": "She sounded in a jocular mood."
    },
    "idiosyncrasy": {
        "definition": "A mode of behavior or way of thought peculiar to an individual.",
        "sentence": "One of his little idiosyncrasies was always preferring to be in the car first."
    },
    "heuristic": {
        "definition": "Enabling a person to discover or learn something for themselves.",
        "sentence": "A heuristic approach to learning."
    },
    "garrulous": {
        "definition": "Excessively talkative, especially on trivial matters.",
        "sentence": "A garrulous cab driver."
    },
    "flabbergasted": {
        "definition": "Surprise (someone) greatly; astonish.",
        "sentence": "This news has left me totally flabbergasted."
    },
    "ephemeral": {
        "definition": "Lasting for a very short time.",
        "sentence": "Fame in the world of rock and roll is largely ephemeral."
    },
    "dilapidated": {
        "definition": "(Of a building or object) in a state of disrepair or ruin as a result of age or neglect.",
        "sentence": "Dilapidated buildings."
    },
    "belligerent": {
        "definition": "Hostile and aggressive.",
        "sentence": "A bull-necked, belligerent old man."
    },
    "aberration": {
        "definition": "A departure from what is normal, usual, or expected, typically an unwelcome one.",
        "sentence": "They described the outbreak of violence in the area as an aberration."
    }
})


# Function to get the word of the week
def get_word_of_the_week(vocab_dict):
    current_week = datetime.date.today().isocalendar()[1]
    words = list(vocab_dict.keys())
    word_of_the_week = words[current_week % len(words)]
    return word_of_the_week, vocab_dict[word_of_the_week]

# Get the word for the current week
word, details = get_word_of_the_week(vocabulary)
print(f"Word of the Week: {word}\nDefinition: {details['definition']}\nExample Sentence: {details['sentence']}")


# Provide the link for pronunciation
search_url = f"https://www.google.com/search?q={word}+pronunciation"
print(f"Click here for the pronunciation: {search_url}")
