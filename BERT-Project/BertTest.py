from bert.BertProcessor import BertProcessor
from evaluator.StoryQualityEvaluator import StoryQualityEvaluator
from utills.VectorUtill import VectorUtill
from scipy.spatial.distance import cosine

## bertProcessor = BertProcessor()
storyQualityEvaluator = StoryQualityEvaluator()

vector = VectorUtill()

p = "Sam and Judy went out for dinner at their favorite restaurant. While driving to the restaurant, Judy’s favorite song played on the radio. Sam found a parking space at the very front of the restaurant. Sam and Judy were seated immediately and ordered their favorite food to the waiter. He looked distracted and tired but was polite while taking their order. Sam’s favorite song played on the radio while they waited for their food. When the waiter returned with their food it was all wrong! The waiter apologized and returned a few minutes later with the correct order. Sam and Judy enjoyed their meal. They paid their tab, left a tip for the waiter, and drove back home."
p2 = "Twenty-two, I was with my first lover, not college-girl exploring but the real deal. She was 28 and had an even older long-distance partner who was visiting, so we went out for coffee drinks. Playing just friends. I’d never had one before; it was divine, sweet Bailey’s flame searing night mocha, whipped cream-topped glass mug, shaved chocolate. Her partner paid, magnanimous, husky and tanned, clueless or so it seemed. I was smug, silky, sitting back watching my lover managing. Later, when she cheated on me too, I called her partner, trying to commiserate. And that was some hot wet salt."
p3 = "Curiosity and intrigue lifelong companions. Shell question everything, even the origin of trees. She fears them at night when the wind races through like a freight train mimicking the clamoring and wailing of voices."
p4 = "She arrived with clenched fists, wide eyes, and strong lungs. During the cleaning, the elders caught her stretching her neck, peering into the darkness of a near past. This would be her lot in life: a bellowing voice, roaming eyes, and a sankofa spirit. Curiosity and intrigue lifelong companions. She’ll question everything, even the origin of trees. She fears them at night when the wind races through like a freight train mimicking the clamoring and wailing of voices. She’ll demand to know who’s there and consider each tap, scratch, and drag a clue, a direct path to the other side."
text = "After stealing money from the bank vault, the bank robber was seen " \
       "fishing on the Mississippi river bank."

p5 = "Confusion and chaos lifted. All was still and clear in his mind. Only hours earlier he was filled with misery, self-loathing and desperation. But now the lycanthropic curse had taken control, freed from its chains and eager to make up for lost time. Jagged claws easily removed the clothes from his body. He would have no more use for them. He had emerged beside a small, shallow river which was painted silver under the clear sky. It was cold, the dead of winter, and his breath misted before his eyes. The weather did not bother him. This body was made for endurance. His long, wiry limbs held easy strength. He felt a buzzing run through his whole body. An electrically charged energy that needed to be unleashed. His magnified senses announced the presence of all living creatures within running distance. None could defy him, none could oppose him. All would flee before him. But it would make no difference. This night would be coloured in blood. He threw back his head and let out a howl of hysteria, elation and fervour. The night belonged to him. The full moon was risen and the chase was on."
p6 = "In eighth grade, I wore tons of make-up to Catholic school. I was a rebel. Trying to hide my outbreaks, I covered them with a layer of Clearasil beneath my beige foundation and powder. But it wasn’t just about my bad complexion. Oh no. I wanted to look like a movie star, like Elizabeth Taylor or Sophia Loren. I penciled in my eyebrows with black eyebrow pencil, jet-black eyeliner thickly lining my eyes, and I topped it all off with jade green eye-shadow that came in a long tube something like a lipstick. My mouth I left blank. This made my eyes stand out more. The fact that we weren’t allowed to wear make-up to school created all this excitement in me, and one day when Sister Theonilla was walking down the aisle in her long black robe, her wire-rim glasses perched on her nose and her skin the color of oatmeal, she stopped at my desk, moved in closer and slowly ran her index finger across my eyelid. The tip of her finger came back green. “I’m not wearing make-up,” I said defiantly. Oh, the thrill of it. This was the beginning of my long career as a liar."
p7 = "It was only 2:00 in the morning. Finding that she could not go back to sleep, she slowly got out of bed and walked downstairs to the kitchen. Putting on an apron, she created the filling by mixing ground pork, chives, minced garlic and soy sauce- amongst other ingredients- together. Then, taking the freshly-kneaded dough, she rolled it into several thin sheets. When the ingredients were prepared, she placed a thin sheet of dough on the palm of her hand and gently scooped up some of the filling-placing it at the center of the dough sheet and pinching the ends of the dough sheet together. That process she repeated until there was no more filling and sheets of dough left. Afterwards, she stir-fried the individually-wrapped fillings in oil until they got crispy. Placing the Chinese dumplings on a plate, she took out a pair of chopsticks and began savoring the taste. When she had a hard time sleeping at night, eating her dumplings would always help. She didn’t really know why, but perhaps it is because they reminded her of her roots; through them, she remembered the old home she used to live in with her family back in China."
storyQualityEvaluator.initiateBertProcess(p)
storyQualityEvaluator.computeMovingCosineSimilarity()
storyQualityEvaluator.plotCosineSimilaritiesBySentenceWord()