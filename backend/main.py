from fastapi import FastAPI
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import json
import re

load_dotenv()
app = FastAPI()
key = os.getenv("API_KEY")
client = genai.Client(api_key=key)

'''
{
    "Question": "What was the main cause of World War II?",
    "Options": [
        "A) The Treaty of Versailles",
        "B) The rise of fascism in Europe",
        "C) The invasion of Poland",
        "D) The attack on Pearl Harbor"
    ],
    "CorrectAnswer": "B) The rise of fascism in Europe"
}
'''
    
# generate questions via Gemini given str content of page
def generateQuestions(text: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Generate a multiple choice question with 4 options and the correct answer based on the following text:
        {text}
        The question should be clear and concise, and the options should be plausible distractors.
        Provide the question, options, and the correct answer in JSON format:

        [
            {{
                "Question": "What was the main cause of World War II?",
                "Options": [
                    "A) The Treaty of Versailles",
                    "B) The rise of fascism in Europe",
                    "C) The invasion of Poland",
                    "D) The attack on Pearl Harbor"
                ],
                "CorrectAnswer": "B) The rise of fascism in Europe"
                "CorrectIndex": 1
            }}
        ]
        """,
    )

    output = response.text
    output = re.sub(r"```json|```", "", output).strip()

    mcqs = json.loads(output)
    print(mcqs)

@app.get("/")
def read_root():
    return "Hello, World... Access Page Here: "

@app.post("/api/generate")
def generate(token: str, content: str):
    return "hello"

generateQuestions(
    '''
    World War II
234 languages
Article
Talk
Read
View source
View history
Tools
Appearance hide
Text
Small
Standard
Large
Width
Standard
Wide
Color (beta)
Automatic
Light
Dark
From Wikipedia, the free encyclopedia
Several terms redirect here. For other uses, see WWII (disambiguation), The Second World War (disambiguation), and World War II (disambiguation).
World War II

From top to bottom, left to right:
German Stuka dive bombers on the Eastern Front, 1943British Matilda II tanks during the North African campaign, 1941US atomic bombing of Nagasaki in Japan, 1945Soviet troops at the Battle of Stalingrad, 1943Soviet soldier raising a flag over the Reichstag after the Battle of Berlin, 1945US warships in Lingayen Gulf in the Philippines, 1945

Date	1 September 1939 – 2 September 1945[a]
(6 years, 1 day)
Location	
Global

Result	
Allied victory

Participants
Allies	Axis
Commanders and leaders
Main Allied leaders:
 Joseph Stalin
 Franklin D. Roosevelt
 Winston Churchill
 Chiang Kai-shek
	Main Axis leaders:
 Adolf Hitler
 Hirohito
 Benito Mussolini

Casualties and losses

Military dead:
Over 16,000,000
Civilian dead:
Over 45,000,000
Total dead:
Over 61,000,000
(1937‍–‍1945)
...further details	
Military dead:
Over 8,000,000
Civilian dead:
Over 4,000,000
Total dead:
Over 12,000,000
(1937‍–‍1945)
...further details
show
vte
Campaigns of World War II


World War II
Navigation

CampaignsCountriesEquipment
TimelineOutlineListsHistoriography
CategoryBibliography

vte

World War II[b] or the Second World War (1 September 1939 – 2 September 1945) was a global conflict between two coalitions: the Allies and the Axis powers. Nearly all of the world's countries participated, with many nations mobilising all resources in pursuit of total war. Tanks and aircraft played major roles, enabling the strategic bombing of cities and delivery of the first and only nuclear weapons ever used in war. World War II is the deadliest conflict in history, causing the death of 70 to 85 million people, more than half of whom were civilians. Millions died in genocides, including the Holocaust, and by massacres, starvation, and disease. After the Allied victory, Germany, Austria, Japan, and Korea were occupied, and German and Japanese leaders were tried for war crimes.

The causes of World War II included unresolved tensions in the aftermath of World War I and the rise of fascism in Europe and militarism in Japan. Key events preceding the war included Japan's invasion of Manchuria in 1931, the Spanish Civil War, the outbreak of the Second Sino-Japanese War in 1937, and Germany's annexations of Austria and the Sudetenland. World War II is generally considered to have begun on 1 September 1939, when Nazi Germany, under Adolf Hitler, invaded Poland, after which the United Kingdom and France declared war on Germany. Poland was divided between Germany and the Soviet Union under the Molotov–Ribbentrop Pact. In 1940, the Soviet Union annexed the Baltic states and parts of Finland and Romania. After the fall of France in June 1940, the war continued mainly between Germany and the British Empire, with fighting in the Balkans, Mediterranean, and Middle East, the aerial Battle of Britain and the Blitz, and the naval Battle of the Atlantic. Through campaigns and treaties, Germany gained control of much of continental Europe and formed the Axis alliance with Italy, Japan, and other countries. In June 1941, Germany invaded the Soviet Union, opening the Eastern Front and initially making large territorial gains.

In December 1941, Japan attacked American and British territories in Asia and the Pacific, including at Pearl Harbor in Hawaii, leading the United States to enter the war against Japan and Germany. Japan conquered much of coastal China and Southeast Asia, but its advances in the Pacific were halted in June 1942 at the Battle of Midway. In early 1943, Axis forces were defeated in North Africa and at Stalingrad in the Soviet Union, and that year their continued defeats on the Eastern Front, an Allied invasion of Italy, and Allied offensives in the Pacific forced them into retreat on all fronts. In 1944, the Western Allies invaded France at Normandy as the Soviet Union recaptured its pre-war territory and the US crippled Japan's navy and captured key Pacific islands. The war in Europe concluded with the liberation of German-occupied territories; invasions of Germany by the Western Allies and the Soviet Union, which culminated in the fall of Berlin to Soviet troops; and Germany's unconditional surrender on 8 May 1945. On 6 and 9 August, the US dropped atomic bombs on Hiroshima and Nagasaki in Japan. Faced with an imminent Allied invasion, the prospect of further atomic bombings, and a Soviet declaration of war and invasion of Manchuria, Japan announced its unconditional surrender on 15 August, and signed a surrender document on 2 September 1945.

World War II transformed the political, economic, and social structures of the world, and established the foundation of international relations for the rest of the 20th century and into the 21st century. The United Nations was created to foster international cooperation and prevent future conflicts, with the victorious great powers—China, France, the Soviet Union, the UK, and the US—becoming the permanent members of its security council. The Soviet Union and the US emerged as rival superpowers, setting the stage for the half-century Cold War. In the wake of Europe's devastation, the influence of its great powers waned, triggering the decolonisation of Africa and of Asia. Many countries whose industries had been damaged moved towards economic recovery and expansion.

Start and end dates
See also: List of timelines of World War II
Timelines of World War II
Chronological

Prelude
Events (in Asiain Europe)
Aftermath


1939194019411942
194319441945Aftermath

By topic

Causes (Diplomacy)
Declarations of war
BattlesOperations

By theatre

Battle of Europe air operations
Eastern FrontManhattan Project
United Kingdom home front
Surrender of the Axis armies

vte

Most historians date the beginning of World War II to the German invasion of Poland on 1 September 1939[1][2] and the United Kingdom and France's declaration of war on Germany two days later. Dates for the beginning of the Pacific War include the start of the Second Sino-Japanese War on 7 July 1937,[3][4] or the earlier Japanese invasion of Manchuria, on 19 September 1931.[5][6] Others follow the British historian A. J. P. Taylor, who stated that the Sino-Japanese War and war in Europe and its colonies occurred simultaneously, and the two wars became World War II in 1941.[7] Other proposed starting dates for World War II include the Italian invasion of Abyssinia on 3 October 1935.[8] The British historian Antony Beevor views the beginning of World War II as the Battles of Khalkhin Gol fought between Japan and the forces of Mongolia and the Soviet Union from May to September 1939.[9] Others view the Spanish Civil War as the start or prelude to World War II.[10][11]

The exact date of the war's end also is not universally agreed upon. It was generally accepted at the time that the war ended with the armistice of 15 August 1945 (V-J Day), rather than with the formal surrender of Japan on 2 September 1945, which officially ended the war in Asia. A peace treaty between Japan and the Allies was signed in 1951.[12] A 1990 treaty regarding Germany's future allowed the reunification of East and West Germany to take place.[13] No formal peace treaty between Japan and the Soviet Union was ever signed,[14] although the state of war between the two countries was terminated by the Soviet–Japanese Joint Declaration of 1956, which also restored full diplomatic relations between them.[15]

Background
Main article: Causes of World War II
Aftermath of World War I
The League of Nations assembly, held in Geneva, Switzerland (1930)

World War I had radically altered the political European map with the defeat of the Central Powers—including Austria-Hungary, Germany, Bulgaria, and the Ottoman Empire—and the 1917 Bolshevik seizure of power in Russia, which led to the founding of the Soviet Union. Meanwhile, the victorious Allies of World War I, such as France, Belgium, Italy, Romania, and Greece, gained territory, and new nation-states were created out of the dissolution of the Austro-Hungarian, Ottoman, and Russian Empires.[16]

To prevent a future world war, the League of Nations was established in 1920 by the Paris Peace Conference. The organisation's primary goals were to prevent armed conflict through collective security, military, and naval disarmament, as well as settling international disputes through peaceful negotiations and arbitration.[17]

Despite strong pacifist sentiment after World War I,[18] irredentist and revanchist nationalism had emerged in several European states. These sentiments were especially marked in Germany because of the significant territorial, colonial, and financial losses imposed by the Treaty of Versailles. Under the treaty, Germany lost around 13 percent of its home territory and all its overseas possessions, while German annexation of other states was prohibited, reparations were imposed, and limits were placed on the size and capability of the country's armed forces.[19]

Germany and Italy

The German Empire was dissolved in the German revolution of 1918–1919, and a democratic government, later known as the Weimar Republic, was created. The interwar period saw strife between supporters of the new republic and hardline opponents on both the political right and left. Italy, as an Entente ally, had made some post-war territorial gains; however, Italian nationalists were angered that the promises made by the United Kingdom and France to secure Italian entrance into the war were not fulfilled in the peace settlement. From 1922 to 1925, the Fascist movement led by Benito Mussolini seized power in Italy with a nationalist, totalitarian, and class collaborationist agenda that abolished representative democracy, repressed socialist, left-wing, and liberal forces, and pursued an aggressive expansionist foreign policy aimed at making Italy a world power, promising the creation of a "New Roman Empire".[20]

Adolf Hitler at a German Nazi political rally in Nuremberg, August 1933

Adolf Hitler, after an unsuccessful attempt to overthrow the German government in 1923, eventually became the chancellor of Germany in 1933 when President Paul von Hindenburg and the Reichstag appointed him. Following Hindenburg's death in 1934, Hitler proclaimed himself Führer of Germany and abolished democracy, espousing a radical, racially motivated revision of the world order, and soon began a massive rearmament campaign.[21] France, seeking to secure its alliance with Italy, allowed Italy a free hand in Ethiopia, which Italy desired as a colonial possession. The situation was aggravated in early 1935 when the Territory of the Saar Basin was legally reunited with Germany, and Hitler repudiated the Treaty of Versailles, accelerated his rearmament programme, and introduced conscription.[22]

European treaties

The United Kingdom, France and Italy formed the Stresa Front in April 1935 in order to contain Germany, a key step towards military globalisation; however, that June, the United Kingdom made an independent naval agreement with Germany, easing prior restrictions. The Soviet Union, concerned by Germany's goals of capturing vast areas of Eastern Europe, drafted a treaty of mutual assistance with France. Before taking effect, though, the Franco-Soviet pact was required to go through the bureaucracy of the League of Nations, which rendered it essentially toothless.[23] The United States, concerned with events in Europe and Asia, passed the Neutrality Act in August of the same year.[24]

Hitler defied the Versailles and Locarno Treaties by remilitarising the Rhineland in March 1936, encountering little opposition due to the policy of appeasement.[25] In October 1936, Germany and Italy formed the Rome–Berlin Axis. A month later, Germany and Japan signed the Anti-Comintern Pact, which Italy joined the following year.[26]

Asia

The Kuomintang party in China launched a unification campaign against regional warlords and nominally unified China in the mid-1920s, but was soon embroiled in a civil war against its former Chinese Communist Party (CCP) allies[27] and new regional warlords. In 1931, an increasingly militaristic Empire of Japan, which had long sought influence in China[28] as the first step of what its government saw as the country's right to rule Asia, staged the Mukden incident as a pretext to invade Manchuria and establish the puppet state of Manchukuo.[29]

China appealed to the League of Nations to stop the Japanese invasion of Manchuria. Japan withdrew from the League of Nations after being condemned for its incursion into Manchuria. The two nations then fought several battles, in Shanghai, Rehe, and Hebei, until the Tanggu Truce was signed in 1933. Thereafter, Chinese volunteer forces continued the resistance to Japanese aggression in Manchuria, and Chahar and Suiyuan.[30] After the 1936 Xi'an Incident, the Kuomintang and CCP forces agreed on a ceasefire to present a united front to oppose Japan.[31]

Pre-war events
Italian invasion of Ethiopia (1935)
Main article: Second Italo-Ethiopian War
Benito Mussolini inspecting troops during the Italo-Ethiopian War, 1935

The Second Italo-Ethiopian War was a brief colonial war that began in October 1935 and ended in May 1936. The war began with the invasion of the Ethiopian Empire (also known as Abyssinia) by the armed forces of the Kingdom of Italy (Regno d'Italia), which was launched from Italian Somaliland and Eritrea.[32] The war resulted in the military occupation of Ethiopia and its annexation into the newly created colony of Italian East Africa (Africa Orientale Italiana); in addition it exposed the weakness of the League of Nations as a force to preserve peace. Both Italy and Ethiopia were member nations, but the League did little when the former clearly violated Article X of the League's Covenant.[33] The United Kingdom and France supported imposing sanctions on Italy for the invasion, but the sanctions were not fully enforced and failed to end the Italian invasion.[34] Italy subsequently dropped its objections to Germany's goal of absorbing Austria.[35]

Spanish Civil War (1936–1939)
Main article: Spanish Civil War

When civil war broke out in Spain, Hitler and Mussolini lent military support to the Nationalist rebels, led by General Francisco Franco. Italy supported the Nationalists to a greater extent than the Nazis: Mussolini sent more than 70,000 ground troops, 6,000 aviation personnel, and 720 aircraft to Spain.[36] The Soviet Union supported the existing government of the Spanish Republic. More than 30,000 foreign volunteers, known as the International Brigades, also fought against the Nationalists. Both Germany and the Soviet Union used this proxy war as an opportunity to test in combat their most advanced weapons and tactics. The Nationalists won the civil war in April 1939; Franco, now dictator, remained officially neutral during World War II but generally favoured the Axis.[37] His greatest collaboration with Germany was the sending of volunteers to fight on the Eastern Front.[38]

Japanese invasion of China (1937)
Main article: Second Sino-Japanese War
Imperial Japanese Army soldiers during the Battle of Shanghai, 1937

In July 1937, Japan captured the former Chinese imperial capital of Peking after instigating the Marco Polo Bridge incident, which culminated in the Japanese campaign to invade all of China.[39] The Soviets quickly signed a non-aggression pact with China to lend materiel support, effectively ending China's prior cooperation with Germany. From September to November, the Japanese attacked Taiyuan, engaged the Kuomintang Army around Xinkou,[40] and fought Communist forces in Pingxingguan.[41][42] Generalissimo Chiang Kai-shek deployed his best army to defend Shanghai, but after three months of fighting, Shanghai fell. The Japanese continued to push Chinese forces back, capturing the capital Nanking in December 1937. After the fall of Nanking, tens or hundreds of thousands of Chinese civilians and disarmed combatants were murdered by the Japanese.[43][44]

In March 1938, Nationalist Chinese forces won their first major victory at Taierzhuang, but then the city of Xuzhou was taken by the Japanese in May.[45] In June 1938, Chinese forces stalled the Japanese advance by flooding the Yellow River; this manoeuvre bought time for the Chinese to prepare their defences at Wuhan, but the city was taken by October.[46] Japanese military victories did not bring about the collapse of Chinese resistance that Japan had hoped to achieve; instead, the Chinese government relocated inland to Chongqing and continued the war.[47][48]

Soviet–Japanese border conflicts
Main article: Soviet–Japanese border conflicts

In the mid-to-late 1930s, Japanese forces in Manchukuo had sporadic border clashes with the Soviet Union and Mongolia. The Japanese doctrine of Hokushin-ron, which emphasised Japan's expansion northward, was favoured by the Imperial Army during this time. This policy would prove difficult to maintain in light of the Japanese defeat at Khalkin Gol in 1939, the ongoing Second Sino-Japanese War[49] and ally Nazi Germany pursuing neutrality with the Soviets. Japan and the Soviet Union eventually signed a Neutrality Pact in April 1941, and Japan adopted the doctrine of Nanshin-ron, promoted by the Navy, which took its focus southward and eventually led to war with the United States and the Western Allies.[50][51]

European occupations and agreements
Chamberlain, Daladier, Hitler, Mussolini, and Ciano pictured just before signing the Munich Agreement, 29 September 1938

In Europe, Germany and Italy were becoming more aggressive. In March 1938, Germany annexed Austria, again provoking little response from other European powers.[52] Encouraged, Hitler began pressing German claims on the Sudetenland, an area of Czechoslovakia with a predominantly ethnic German population. Soon the United Kingdom and France followed the appeasement policy of British Prime Minister Neville Chamberlain and conceded this territory to Germany in the Munich Agreement, which was made against the wishes of the Czechoslovak government, in exchange for a promise of no further territorial demands.[53] Soon afterwards, Germany and Italy forced Czechoslovakia to cede additional territory to Hungary, and Poland annexed the Trans-Olza region of Czechoslovakia.[54]

Although all of Germany's stated demands had been satisfied by the agreement, privately Hitler was furious that British interference had prevented him from seizing all of Czechoslovakia in one operation. In subsequent speeches Hitler attacked British and Jewish "war-mongers" and in January 1939 secretly ordered a major build-up of the German navy to challenge British naval supremacy. In March 1939, Germany invaded the remainder of Czechoslovakia and subsequently split it into the German Protectorate of Bohemia and Moravia and a pro-German client state, the Slovak Republic.[55] Hitler also delivered an ultimatum to Lithuania on 20 March 1939, forcing the concession of the Klaipėda Region, formerly the German Memelland.[56]

German Foreign Minister Joachim von Ribbentrop (right) and the Soviet leader Joseph Stalin, after signing the Molotov–Ribbentrop Pact, 23 August 1939

Greatly alarmed and with Hitler making further demands on the Free City of Danzig, the United Kingdom and France guaranteed their support for Polish independence; when Italy conquered Albania in April 1939, the same guarantee was extended to the Kingdoms of Romania and Greece.[57] Shortly after the Franco-British pledge to Poland, Germany and Italy formalised their own alliance with the Pact of Steel.[58] Hitler accused the United Kingdom and Poland of trying to "encircle" Germany and renounced the Anglo-German Naval Agreement and the German–Polish declaration of non-aggression.[59]

The situation became a crisis in late August as German troops continued to mobilise against the Polish border. On 23 August the Soviet Union signed a non-aggression pact with Germany,[60] after tripartite negotiations for a military alliance between France, the United Kingdom, and Soviet Union had stalled.[61] This pact had a secret protocol that defined German and Soviet "spheres of influence" (western Poland and Lithuania for Germany; eastern Poland, Finland, Estonia, Latvia and Bessarabia for the Soviet Union), and raised the question of continuing Polish independence.[62] The pact neutralised the possibility of Soviet opposition to a campaign against Poland and assured that Germany would not have to face the prospect of a two-front war, as it had in World War I. Immediately afterwards, Hitler ordered the attack to proceed on 26 August, but upon hearing that the United Kingdom had concluded a formal mutual assistance pact with Poland and that Italy would maintain neutrality, he decided to delay it.[63]

In response to British requests for direct negotiations to avoid war, Germany made demands on Poland, which served as a pretext to worsen relations.[64] On 29 August, Hitler demanded that a Polish plenipotentiary immediately travel to Berlin to negotiate the handover of Danzig, and to allow a plebiscite in the Polish Corridor in which the German minority would vote on secession.[64] The Poles refused to comply with the German demands, and on the night of 30–31 August in a confrontational meeting with the British ambassador Nevile Henderson, Ribbentrop declared that Germany considered its claims rejected.[65]

Course of the war
For a chronological guide, see List of timelines of World War II.
See also: Diplomatic history of World War II and World War II by country
War breaks out in Europe (1939–1940)
Main article: European theatre of World War II
A German propaganda photo reenacting the removal of the Polish border crossing in Sopot[66]

On 1 September 1939, Germany invaded Poland after having staged several false flag border incidents as a pretext to initiate the invasion.[67] The first German attack of the war came against the Polish defences at Westerplatte.[68] The United Kingdom responded with an ultimatum for Germany to cease military operations, and on 3 September, after the ultimatum was ignored, Britain and France declared war on Germany.[c] During the Phoney War period, the alliance provided no direct military support to Poland, outside of a cautious French probe into the Saarland.[69] The Western Allies also began a naval blockade of Germany, which aimed to damage the country's economy and war effort.[70] Germany responded by ordering U-boat warfare against Allied merchant and warships, which would later escalate into the Battle of the Atlantic.[71] On 8 September, German troops reached the suburbs of Warsaw. The Polish counter-offensive to the west halted the German advance for several days, but it was outflanked and encircled by the Wehrmacht. Remnants of the Polish army broke through to besieged Warsaw. On 17 September 1939, two days after signing a cease-fire with Japan, the Soviet Union invaded Poland[72] under the supposed pretext that the Polish state had ceased to exist.[73] On 27 September, the Warsaw garrison surrendered to the Germans, and the last large operational unit of the Polish Army surrendered on 6 October. Despite the military defeat, Poland never surrendered; instead, it formed the Polish government-in-exile and a clandestine state apparatus remained in occupied Poland.[74] A significant part of Polish military personnel evacuated to Romania and Latvia; many of them later fought against the Axis in other theatres of the war.[75]

Germany annexed western Poland and occupied central Poland; the Soviet Union annexed eastern Poland; small shares of Polish territory were transferred to Lithuania and Slovakia. On 6 October, Hitler made a public peace overture to the United Kingdom and France but said that the future of Poland was to be determined exclusively by Germany and the Soviet Union. The proposal was rejected[65] and Hitler ordered an immediate offensive against France,[76] which was postponed until the spring of 1940 due to bad weather.[77][78][79]

Mannerheim Line and Karelian Isthmus on the last day of the Winter War, 13 March 1940

After the outbreak of war in Poland, Stalin threatened Estonia, Latvia, and Lithuania with military invasion, forcing the three Baltic countries to sign pacts allowing the creation of Soviet military bases in these countries; in October 1939, significant Soviet military contingents were moved there.[80][81][82] Finland refused to sign a similar pact and rejected ceding part of its territory to the Soviet Union. The Soviet Union invaded Finland in November 1939,[83] and was subsequently expelled from the League of Nations for this crime of aggression.[84] Despite overwhelming numerical superiority, Soviet military success during the Winter War was modest, and the Finno-Soviet war ended in March 1940 with some Finnish concessions of territory.[85]

In June 1940, the Soviet Union occupied the entire territories of Estonia, Latvia and Lithuania,[81] as well as the Romanian regions of Bessarabia, Northern Bukovina, and the Hertsa region. In August 1940, Hitler imposed the Second Vienna Award on Romania which led to the transfer of Northern Transylvania to Hungary.[86] In September 1940, Bulgaria demanded Southern Dobruja from Romania with German and Italian support, leading to the Treaty of Craiova.[87] The loss of one-third of Romania's 1939 territory caused a coup against King Carol II, turning Romania into a fascist dictatorship under Marshal Ion Antonescu, with a course set towards the Axis in the hopes of a German guarantee.[88] Meanwhile, German-Soviet political relations and economic co-operation[89][90] gradually stalled,[91][92] and both states began preparations for war.[93]

Western Europe (1940–1941)
Main article: Western Front (World War II)
German advance into Belgium and Northern France, 10 May – 4 June 1940, sweeping past the Maginot Line (shown in dark red)

In April 1940, Germany invaded Denmark and Norway to protect shipments of iron ore from Sweden, which the Allies were attempting to cut off.[94] Denmark capitulated after six hours, and despite Allied support, Norway was conquered within two months.[95] British discontent over the Norwegian campaign led to the resignation of Prime Minister Neville Chamberlain, who was replaced by Winston Churchill on 10 May 1940.[96]

On the same day, Germany launched an offensive against France. To circumvent the strong Maginot Line fortifications on the Franco-German border, Germany directed its attack at the neutral nations of Belgium, the Netherlands, and Luxembourg.[97] The Germans carried out a flanking manoeuvre through the Ardennes region,[98] which was mistakenly perceived by the Allies as an impenetrable natural barrier against armoured vehicles.[99][100] By successfully implementing new Blitzkrieg tactics, the Wehrmacht rapidly advanced to the Channel and cut off the Allied forces in Belgium, trapping the bulk of the Allied armies in a cauldron on the Franco-Belgian border near Lille. The United Kingdom was able to evacuate a significant number of Allied troops from the continent by early June, although they had to abandon almost all their equipment.[101]

On 10 June, Italy invaded France, declaring war on both France and the United Kingdom.[102] The Germans turned south against the weakened French army, and Paris fell to them on 14 June. Eight days later France signed an armistice with Germany; it was divided into German and Italian occupation zones,[103] and an unoccupied rump state under the Vichy Regime, which, though officially neutral, was generally aligned with Germany. France kept its fleet, which the United Kingdom attacked on 3 July in an attempt to prevent its seizure by Germany.[104]

The air Battle of Britain[105] began in early July with Luftwaffe attacks on shipping and harbours.[106] The German campaign for air superiority started in August but its failure to defeat RAF Fighter Command forced the indefinite postponement of the proposed German invasion of Britain. The German strategic bombing offensive intensified with night attacks on London and other cities in the Blitz, but largely ended in May 1941[107] after failing to significantly disrupt the British war effort.[106]

Using newly captured French ports, the German Navy enjoyed success against an over-extended Royal Navy, using U-boats against British shipping in the Atlantic.[108] The British Home Fleet scored a significant victory on 27 May 1941 by sinking the German battleship Bismarck.[109]

In November 1939, the United States was assisting China and the Western Allies, and had amended the Neutrality Act to allow "cash and carry" purchases by the Allies.[110] In 1940, following the German capture of Paris, the size of the United States Navy was significantly increased. In September the United States further agreed to a trade of American destroyers for British bases.[111] Still, a large majority of the American public continued to oppose any direct military intervention in the conflict well into 1941.[112] In December 1940, Roosevelt accused Hitler of planning world conquest and ruled out any negotiations as useless, calling for the United States to become an "arsenal of democracy" and promoting Lend-Lease programmes of military and humanitarian aid to support the British war effort; Lend-Lease was later extended to the other Allies, including the Soviet Union after it was invaded by Germany.[113] The United States started strategic planning to prepare for a full-scale offensive against Germany.[114]

At the end of September 1940, the Tripartite Pact formally united Japan, Italy, and Germany as the Axis powers. The Tripartite Pact stipulated that any country—with the exception of the Soviet Union—that attacked any Axis Power would be forced to go to war against all three.[115] The Axis expanded in November 1940 when Hungary, Slovakia, and Romania joined.[116] Romania and Hungary later made major contributions to the Axis war against the Soviet Union, in Romania's case partially to recapture territory ceded to the Soviet Union.[117]

Mediterranean (1940–1941)
Main article: Mediterranean and Middle East theatre of World War II

In early June 1940, the Italian Regia Aeronautica attacked and besieged Malta, a British possession. From late summer to early autumn, Italy conquered British Somaliland and made an incursion into British-held Egypt. In October, Italy attacked Greece, but the attack was repulsed with heavy Italian casualties; the campaign ended within months with minor territorial changes.[118] To assist Italy and prevent Britain from gaining a foothold, Germany prepared to invade the Balkans, which would threaten Romanian oil fields and strike against British dominance of the Mediterranean.[119]

German Panzer III of the Afrika Korps advancing across the North African desert, April 1941

In December 1940, British Empire forces began counter-offensives against Italian forces in Egypt and Italian East Africa.[120] The offensives were successful; by early February 1941, Italy had lost control of eastern Libya, and large numbers of Italian troops had been taken prisoner. The Italian Navy also suffered significant defeats, with the Royal Navy putting three Italian battleships out of commission after a carrier attack at Taranto, and neutralising several more warships at the Battle of Cape Matapan.[121]

Italian defeats prompted Germany to deploy an expeditionary force to North Africa; at the end of March 1941, Rommel's Afrika Korps launched an offensive which drove back Commonwealth forces.[122] In less than a month, Axis forces advanced to western Egypt and besieged the port of Tobruk.[123]

By late March 1941, Bulgaria and Yugoslavia signed the Tripartite Pact; however, the Yugoslav government was overthrown two days later by pro-British nationalists. Germany and Italy responded with simultaneous invasions of both Yugoslavia and Greece, commencing on 6 April 1941; both nations were forced to surrender within the month.[124] The airborne invasion of the Greek island of Crete at the end of May completed the German conquest of the Balkans.[125] Partisan warfare subsequently broke out against the Axis occupation of Yugoslavia, which continued until the end of the war.[126]

In the Middle East in May, Commonwealth forces quashed an uprising in Iraq which had been supported by German aircraft from bases within Vichy-controlled Syria.[127] Between June and July, British-led forces invaded and occupied the French possessions of Syria and Lebanon, assisted by the Free French.[128]

Axis attack on the Soviet Union (1941)
Main article: Eastern Front (World War II)
European theatre of World War II animation map, 1939–1945 – Red: Western Allies and the Soviet Union after 1941; Green: Soviet Union before 1941; Blue: Axis powers

With the situation in Europe and Asia relatively stable, Germany, Japan, and the Soviet Union made preparations for war. With the Soviets wary of mounting tensions with Germany, and the Japanese planning to take advantage of the European War by seizing resource-rich European possessions in Southeast Asia, the two powers signed the Soviet–Japanese Neutrality Pact in April 1941.[129] By contrast, the Germans were steadily making preparations for an attack on the Soviet Union, massing forces on the Soviet border.[130]

Hitler believed that the United Kingdom's refusal to end the war was based on the hope that the United States and the Soviet Union would enter the war against Germany sooner or later.[131] On 31 July 1940, Hitler decided that the Soviet Union should be eliminated and aimed for the conquest of Ukraine, the Baltic states and Byelorussia.[132] However, other senior German officials like Ribbentrop saw an opportunity to create a Euro-Asian bloc against the British Empire by inviting the Soviet Union into the Tripartite Pact.[133] In November 1940, negotiations took place to determine if the Soviet Union would join the pact. The Soviets showed some interest but asked for concessions from Finland, Bulgaria, Turkey, and Japan that Germany considered unacceptable. On 18 December 1940, Hitler issued the directive to prepare for an invasion of the Soviet Union.[134]

On 22 June 1941, Germany, supported by Italy and Romania, invaded the Soviet Union in Operation Barbarossa, with Germany accusing the Soviets of plotting against them; they were joined shortly by Finland and Hungary.[135] The primary targets of this surprise offensive[136] were the Baltic region, Moscow and Ukraine, with the ultimate goal of ending the 1941 campaign near the Arkhangelsk–Astrakhan line—from the Caspian to the White Seas. Hitler's objectives were to eliminate the Soviet Union as a military power, exterminate Communism, generate Lebensraum ("living space")[137] by dispossessing the native population,[138] and guarantee access to the strategic resources needed to defeat Germany's remaining rivals.[139]

Although the Red Army was preparing for strategic counter-offensives before the war,[140] Operation Barbarossa forced the Soviet supreme command to adopt strategic defence. During the summer, the Axis made significant gains into Soviet territory, inflicting immense losses in both personnel and materiel. By mid-August, however, the German Army High Command decided to suspend the offensive of a considerably depleted Army Group Centre, and to divert the 2nd Panzer Group to reinforce troops advancing towards central Ukraine and Leningrad.[141] The Kiev offensive was overwhelmingly successful, resulting in encirclement and elimination of four Soviet armies, and made possible further advance into Crimea and industrially-developed Eastern Ukraine (the First Battle of Kharkov).[142]

Russian civilians leaving destroyed houses after a German bombardment during the siege of Leningrad (Saint Petersburg), 10 December 1942

The diversion of three-quarters of the Axis troops and the majority of their air forces from France and the central Mediterranean to the Eastern Front[143] prompted the United Kingdom to reconsider its grand strategy.[144] In July, the UK and the Soviet Union formed a military alliance against Germany[145] and in August, the United Kingdom and the United States jointly issued the Atlantic Charter, which outlined British and American goals for the post-war world.[146] In late August the British and Soviets invaded neutral Iran to secure the Persian Corridor, Iran's oil fields, and preempt any Axis advances through Iran toward the Baku oil fields or India.[147]

By October, Axis powers had achieved operational objectives in Ukraine and the Baltic region, with only the sieges of Leningrad[148] and Sevastopol continuing.[149] A major offensive against Moscow was renewed; after two months of fierce battles in increasingly harsh weather, the German army almost reached the outer suburbs of Moscow, where the exhausted troops[150] were forced to suspend the offensive.[151] Large territorial gains were made by Axis forces, but their campaign had failed to achieve its main objectives: two key cities remained in Soviet hands, the Soviet capability to resist was not broken, and the Soviet Union retained a considerable part of its military potential. The blitzkrieg phase of the war in Europe had ended.[152]

By early December, freshly mobilised reserves[153] allowed the Soviets to achieve numerical parity with Axis troops.[154] This, as well as intelligence data which established that a minimal number of Soviet troops in the East would be sufficient to deter any attack by the Japanese Kwantung Army,[155] allowed the Soviets to begin a massive counter-offensive that started on 5 December all along the front and pushed German troops 100–250 kilometres (62–155 mi) west.[156]

War breaks out in the Pacific (1941)
Main article: Pacific War
Japanese soldiers entering Hong Kong, 8 December 1941

Following the Japanese false flag Mukden incident in 1931, the Japanese shelling of the American gunboat USS Panay in 1937, and the 1937–1938 Nanjing Massacre, Japanese-American relations deteriorated. In 1939, the United States notified Japan that it would not be extending its trade treaty and American public opinion opposing Japanese expansionism led to a series of economic sanctions—the Export Control Acts—which banned US exports of chemicals, minerals and military parts to Japan, and increased economic pressure on the Japanese regime.[113][157][158] During 1939 Japan launched its first attack against Changsha, but was repulsed by late September.[159] Despite several offensives by both sides, by 1940 the war between China and Japan was at a stalemate. To increase pressure on China by blocking supply routes, and to better position Japanese forces in the event of a war with the Western powers, Japan invaded and occupied northern Indochina in September 1940.[160]

Chinese nationalist forces launched a large-scale counter-offensive in early 1940. In August, Chinese communists launched an offensive in Central China;[161] in retaliation, Japan instituted harsh measures in occupied areas to reduce human and material resources for the communists.[162] Continued antipathy between Chinese communist and nationalist forces culminated in armed clashes in January 1941, effectively ending their co-operation.[163] In March, the Japanese 11th army attacked the headquarters of the Chinese 19th army but was repulsed during the Battle of Shanggao.[164] In September, Japan attempted to take the city of Changsha again and clashed with Chinese nationalist forces.[165]

German successes in Europe prompted Japan to increase pressure on European governments in Southeast Asia. The Dutch government agreed to provide Japan with oil supplies from the Dutch East Indies, but negotiations for additional access to their resources ended in failure in June 1941.[166] In July 1941 Japan sent troops to southern Indochina, thus threatening British and Dutch possessions in the Far East. The United States, the United Kingdom, and other Western governments reacted to this move with a freeze on Japanese assets and a total oil embargo.[167][168] At the same time, Japan was planning an invasion of the Soviet Far East, intending to take advantage of the German invasion in the west, but abandoned the operation after the sanctions.[169]

Since early 1941, the United States and Japan had been engaged in negotiations in an attempt to improve their strained relations and end the war in China. During these negotiations, Japan advanced a number of proposals which were dismissed by the Americans as inadequate.[170] At the same time the United States, the United Kingdom, and the Netherlands engaged in secret discussions for the joint defence of their territories, in the event of a Japanese attack against any of them.[171] Roosevelt reinforced the Philippines (an American protectorate scheduled for independence in 1946) and warned Japan that the United States would react to Japanese attacks against any "neighboring countries".[171]

The USS Arizona was a total loss in the Japanese surprise air attack on the United States Pacific Fleet at Pearl Harbor, Sunday 7 December 1941

Frustrated at the lack of progress and feeling the pinch of the American–British–Dutch sanctions, Japan prepared for war. Emperor Hirohito, after initial hesitation about Japan's chances of victory,[172] began to favour Japan's entry into the war.[173] As a result, Prime Minister Fumimaro Konoe resigned.[174][175] Hirohito refused the recommendation to appoint Prince Naruhiko Higashikuni in his place, choosing War Minister Hideki Tojo instead.[176] On 3 November, Nagano explained in detail the plan of the attack on Pearl Harbor to the Emperor.[177] On 5 November, Hirohito approved in imperial conference the operations plan for the war.[178] On 20 November, the new government presented an interim proposal as its final offer. It called for the end of American aid to China and for lifting the embargo on the supply of oil and other resources to Japan. In exchange, Japan promised not to launch any attacks in Southeast Asia and to withdraw its forces from southern Indochina.[170] The American counter-proposal of 26 November required that Japan evacuate all of China without conditions and conclude non-aggression pacts with all Pacific powers.[179] That meant Japan was essentially forced to choose between abandoning its ambitions in China, or seizing the natural resources it needed in the Dutch East Indies by force;[180][181] the Japanese military did not consider the former an option, and many officers considered the oil embargo an unspoken declaration of war.[182]

Japan planned to seize European colonies in Asia to create a large defensive perimeter stretching into the Central Pacific. The Japanese would then be free to exploit the resources of Southeast Asia while exhausting the over-stretched Allies by fighting a defensive war.[183][184] To prevent American intervention while securing the perimeter, it was further planned to neutralise the United States Pacific Fleet and the American military presence in the Philippines from the outset.[185] On 7 December 1941 (8 December in Asian time zones), Japan attacked British and American holdings with near-simultaneous offensives against Southeast Asia and the Central Pacific.[186] These included an attack on the American fleets at Pearl Harbor and the Philippines, as well as invasions of Guam, Wake Island, Malaya,[186] Thailand, and Hong Kong.[187]

These attacks led the United States, United Kingdom, China, Australia, and several other states to formally declare war on Japan, whereas the Soviet Union, being heavily involved in large-scale hostilities with European Axis countries, maintained its neutrality agreement with Japan.[188] Germany, followed by the other Axis states, declared war on the United States[189] in solidarity with Japan, citing as justification the American attacks on German war vessels that had been ordered by Roosevelt.[135][190]

Axis advance stalls (1942–1943)

On 1 January 1942, the Allied Big Four[191]—the Soviet Union, China, the United Kingdom, and the United States—and 22 smaller or exiled governments issued the Declaration by United Nations, thereby affirming the Atlantic Charter[192] and agreeing not to sign a separate peace with the Axis powers.[193]

During 1942, Allied officials debated on the appropriate grand strategy to pursue. All agreed that defeating Germany was the primary objective. The Americans favoured a straightforward, large-scale attack on Germany through France. The Soviets demanded a second front. The British argued that military operations should target peripheral areas to wear out German strength, leading to increasing demoralisation, and bolstering resistance forces; Germany itself would be subject to a heavy bombing campaign. An offensive against Germany would then be launched primarily by Allied armour, without using large-scale armies.[194] Eventually, the British persuaded the Americans that a landing in France was infeasible in 1942 and they should instead focus on driving the Axis out of North Africa.[195]

At the Casablanca Conference in early 1943, the Allies reiterated the statements issued in the 1942 Declaration and demanded the unconditional surrender of their enemies. The British and Americans agreed to continue to press the initiative in the Mediterranean by invading Sicily to fully secure the Mediterranean supply routes.[196] Although the British argued for further operations in the Balkans to bring Turkey into the war, in May 1943, the Americans extracted a British commitment to limit Allied operations in the Mediterranean to an invasion of the Italian mainland, and to invade France in 1944.[197]

Pacific (1942–1943)
Map of Japanese military advances through mid-1942

By the end of April 1942, Japan and its ally Thailand had almost conquered Burma, Malaya, the Dutch East Indies, Singapore, and Rabaul, inflicting severe losses on Allied troops and taking a large number of prisoners.[198] Despite stubborn resistance by Filipino and US forces, the Philippine Commonwealth was eventually captured in May 1942, forcing its government into exile.[199] On 16 April, in Burma, 7,000 British soldiers were encircled by the Japanese 33rd Division during the Battle of Yenangyaung and rescued by the Chinese 38th Division.[200] Japanese forces also achieved naval victories in the South China Sea, Java Sea, and Indian Ocean,[201] and bombed the Allied naval base at Darwin, Australia. In January 1942, the only Allied success against Japan was a Chinese victory at Changsha.[202] These easy victories over the unprepared US and European opponents left Japan overconfident, and overextended.[203]

In early May 1942, Japan initiated operations to capture Port Moresby by amphibious assault and thus sever communications and supply lines between the United States and Australia. The planned invasion was thwarted when an Allied task force, centred on two American fleet carriers, fought Japanese naval forces to a draw in the Battle of the Coral Sea.[204] Japan's next plan, motivated by the earlier Doolittle Raid, was to seize Midway Atoll and lure American carriers into battle to be eliminated; as a diversion, Japan would also send forces to occupy the Aleutian Islands in Alaska.[205] In mid-May, Japan started the Zhejiang-Jiangxi campaign in China, with the goal of inflicting retribution on the Chinese who aided the surviving American airmen in the Doolittle Raid by destroying Chinese air bases and fighting against the Chinese 23rd and 32nd Army Groups.[206][207] In early June, Japan put its operations into action, but the Americans had broken Japanese naval codes in late May and were fully aware of the plans and order of battle, and used this knowledge to achieve a decisive victory at Midway over the Imperial Japanese Navy.[208]

With its capacity for aggressive action greatly diminished as a result of the Midway battle, Japan attempted to capture Port Moresby by an overland campaign in the Territory of Papua.[209] The Americans planned a counterattack against Japanese positions in the southern Solomon Islands, primarily Guadalcanal, as a first step towards capturing Rabaul, the main Japanese base in Southeast Asia.[210]

Both plans started in July, but by mid-September, the Battle for Guadalcanal took priority for the Japanese, and troops in New Guinea were ordered to withdraw from the Port Moresby area to the northern part of the island, where they faced Australian and United States troops in the Battle of Buna–Gona.[211] Guadalcanal soon became a focal point for both sides with heavy commitments of troops and ships in the battle for Guadalcanal. By the start of 1943, the Japanese were defeated on the island and withdrew their troops.[212] In Burma, Commonwealth forces mounted two operations. The first was a disastrous offensive into the Arakan region in late 1942 that forced a retreat back to India by May 1943.[213] The second was the insertion of irregular forces behind Japanese frontlines in February which, by the end of April, had achieved mixed results.[214]

Eastern Front (1942–1943)
Red Army soldiers on the counterattack during the Battle of Stalingrad, February 1943

Despite considerable losses, in early 1942 Germany and its allies stopped a major Soviet offensive in central and southern Russia, keeping most territorial gains they had achieved during the previous year.[215] In May, the Germans defeated Soviet offensives in the Kerch Peninsula and at Kharkov,[216] and then in June 1942 launched their main summer offensive against southern Russia, to seize the oil fields of the Caucasus and occupy the Kuban steppe, while maintaining positions on the northern and central areas of the front. The Germans split Army Group South into two groups: Army Group A advanced to the lower Don River and struck south-east to the Caucasus, while Army Group B headed towards the Volga River. The Soviets decided to make their stand at Stalingrad on the Volga.[217]

By mid-November, the Germans had nearly taken Stalingrad in bitter street fighting. The Soviets began their second winter counter-offensive, starting with an encirclement of German forces at Stalingrad,[218] and an assault on the Rzhev salient near Moscow, though the latter failed disastrously.[219] By early February 1943, the German Army had taken tremendous losses; German troops at Stalingrad had been defeated,[220] and the front-line had been pushed back beyond its position before the summer offensive. In mid-February, after the Soviet push had tapered off, the Germans launched another attack on Kharkov, creating a salient in their front line around the Soviet city of Kursk.[221]

Western Europe/Atlantic and Mediterranean (1942–1943)
American Eighth Air Force Boeing B-17 Flying Fortress bombing raid on the Focke-Wulf factory in Germany, 9 October 1943

Exploiting poor American naval command decisions, the German navy ravaged Allied shipping off the American Atlantic coast.[222] By November 1941, Commonwealth forces had launched a counter-offensive in North Africa, Operation Crusader, and reclaimed all the gains the Germans and Italians had made.[223] The Germans also launched a North African offensive in January, pushing the British back to positions at the Gazala line by early February,[224] followed by a temporary lull in combat which Germany used to prepare for their upcoming offensives.[225] Concerns that the Japanese might use bases in Vichy-held Madagascar caused the British to invade the island in early May 1942.[226] An Axis offensive in Libya forced an Allied retreat deep inside Egypt until Axis forces were stopped at El Alamein.[227] On the Continent, raids of Allied commandos on strategic targets, culminating in the failed Dieppe Raid,[228] demonstrated the Western Allies' inability to launch an invasion of continental Europe without much better preparation, equipment, and operational security.[229]

In August 1942, the Allies succeeded in repelling a second attack against El Alamein[230] and, at a high cost, managed to deliver desperately needed supplies to the besieged Malta.[231] A few months later, the Allies commenced an attack of their own in Egypt, dislodging the Axis forces and beginning a drive west across Libya.[232] This attack was followed up shortly after by Anglo-American landings in French North Africa, which resulted in the region joining the Allies.[233] Hitler responded to the French colony's defection by ordering the occupation of Vichy France;[233] although Vichy forces did not resist this violation of the armistice, they managed to scuttle their fleet to prevent its capture by German forces.[233][234] Axis forces in Africa withdrew into Tunisia, which was conquered by the Allies in May 1943.[233][235]

In June 1943, the British and Americans began a strategic bombing campaign against Germany with a goal to disrupt the war economy, reduce morale, and "de-house" the civilian population.[236] The firebombing of Hamburg was among the first attacks in this campaign, inflicting significant casualties and considerable losses on infrastructure of this important industrial centre.[237]

Allies gain momentum (1943–1944)
US Navy SBD-5 scout plane flying patrol over USS Washington and USS Lexington during the Gilbert and Marshall Islands campaign, 1943

After the Guadalcanal campaign, the Allies initiated several operations against Japan in the Pacific. In May 1943, Canadian and US forces were sent to eliminate Japanese forces from the Aleutians.[238] Soon after, the United States, with support from Australia, New Zealand and Pacific Islander forces, began major ground, sea and air operations to isolate Rabaul by capturing surrounding islands, and breach the Japanese Central Pacific perimeter at the Gilbert and Marshall Islands.[239] By the end of March 1944, the Allies had completed both of these objectives and had also neutralised the major Japanese base at Truk in the Caroline Islands. In April, the Allies launched an operation to retake Western New Guinea.[240]

In the Soviet Union, both the Germans and the Soviets spent the spring and early summer of 1943 preparing for large offensives in central Russia. On 5 July 1943, Germany attacked Soviet forces around the Kursk Bulge. Within a week, German forces had exhausted themselves against the Soviets' well-constructed defences,[241] and for the first time in the war, Hitler cancelled an operation before it had achieved tactical or operational success.[242] This decision was partially affected by the Western Allies' invasion of Sicily launched on 9 July, which, combined with previous Italian failures, resulted in the ousting and arrest of Mussolini later that month.[243]

On 12 July 1943, the Soviets launched their own counter-offensives, thereby dispelling any chance of German victory or even stalemate in the east. The Soviet victory at Kursk marked the end of German superiority,[244] giving the Soviet Union the initiative on the Eastern Front.[245][246] The Germans tried to stabilise their eastern front along the hastily fortified Panther–Wotan line, but the Soviets broke through it at Smolensk and the Lower Dnieper Offensive.[247]

On 3 September 1943, the Western Allies invaded the Italian mainland, following Italy's armistice with the Allies and the ensuing German occupation of Italy.[248] Germany, with the help of fascists, responded to the armistice by disarming Italian forces that were in many places without superior orders, seizing military control of Italian areas,[249] and creating a series of defensive lines.[250] German special forces then rescued Mussolini, who then soon established a new client state in German-occupied Italy named the Italian Social Republic,[251] causing an Italian civil war. The Western Allies fought through several lines until reaching the main German defensive line in mid-November.[252]

Red Army troops in a counter-offensive on German positions at the Battle of Kursk, July 1943

German operations in the Atlantic also suffered. By May 1943, as Allied counter-measures became increasingly effective, the resulting sizeable German submarine losses forced a temporary halt of the German Atlantic naval campaign.[253] In November 1943, Franklin D. Roosevelt and Winston Churchill met with Chiang Kai-shek in Cairo and then with Joseph Stalin in Tehran.[254] The former conference determined the post-war return of Japanese territory[255] and the military planning for the Burma campaign,[256] while the latter included agreement that the Western Allies would invade Europe in 1944 and that the Soviet Union would declare war on Japan within three months of Germany's defeat.[257]

From November 1943, during the seven-week Battle of Changde, the Chinese awaited allied relief as they forced Japan to fight a costly war of attrition.[258][259][260] In January 1944, the Allies launched a series of attacks in Italy against the line at Monte Cassino and tried to outflank it with landings at Anzio.[261]

On 27 January 1944, Soviet troops launched a major offensive that expelled German forces from the Leningrad region, thereby ending the most lethal siege in history.[262] The following Soviet offensive was halted on the pre-war Estonian border by the German Army Group North aided by Estonians hoping to re-establish national independence. This delay slowed subsequent Soviet operations in the Baltic Sea region.[263] By late May 1944, the Soviets had liberated Crimea, largely expelled Axis forces from Ukraine, and made incursions into Romania, which were repulsed by the Axis troops.[264] The Allied offensives in Italy had succeeded and, at the expense of allowing several German divisions to retreat, Rome was captured on 4 June.[265]

The Allies had mixed success in mainland Asia. In March 1944, the Japanese launched the first of two invasions, an operation against Allied positions in Assam, India,[266] and soon besieged Commonwealth positions at Imphal and Kohima.[267] In May 1944, British and Indian forces mounted a counter-offensive that drove Japanese troops back to Burma by July,[267] and Chinese forces that had invaded northern Burma in late 1943 besieged Japanese troops in Myitkyina.[268] The second Japanese invasion of China aimed to destroy China's main fighting forces, secure railways between Japanese-held territory and capture Allied airfields.[269] By June, the Japanese had conquered the province of Henan and begun a new attack on Changsha.[270]

Allies close in (1944)
American troops approaching Omaha Beach during the invasion of Normandy on D-Day, 6 June 1944

On 6 June 1944 (commonly known as D-Day), after three years of Soviet pressure,[271] the Western Allies invaded northern France. After reassigning several Allied divisions from Italy, they also attacked southern France.[272] These landings were successful and led to the defeat of the German Army units in France. Paris was liberated on 25 August by the local resistance assisted by the Free French Forces, both led by General Charles de Gaulle,[273] and the Western Allies continued to push back German forces in western Europe during the latter part of the year. An attempt to advance into northern Germany spearheaded by a major airborne operation in the Netherlands failed.[274] After that, the Western Allies slowly pushed into Germany, but failed to cross the Ruhr river. In Italy, the Allied advance slowed due to the last major German defensive line.[275]

On 22 June, the Soviets launched a strategic offensive in Belarus ("Operation Bagration") that nearly destroyed the German Army Group Centre.[276] Soon after that, another Soviet strategic offensive forced German troops from Western Ukraine and Eastern Poland. The Soviets formed the Polish Committee of National Liberation to control territory in Poland and combat the Polish Armia Krajowa; the Soviet Red Army remained in the Praga district on the other side of the Vistula and watched passively as the Germans quelled the Warsaw Uprising initiated by the Armia Krajowa.[277] The national uprising in Slovakia was also quelled by the Germans.[278] The Soviet Red Army's strategic offensive in eastern Romania cut off and destroyed the considerable German troops there and triggered a successful coup d'état in Romania and in Bulgaria, followed by those countries' shift to the Allied side.[279]

General Douglas MacArthur returns to the Philippines during the Battle of Leyte, 20 October 1944

In September 1944, Soviet troops advanced into Yugoslavia and forced the rapid withdrawal of German Army Groups E and F in Greece, Albania, and Yugoslavia to rescue them from being cut off.[280] By this point, the communist-led Partisans under Marshal Josip Broz Tito, who had led an increasingly successful guerrilla campaign against the occupation since 1941, controlled much of the territory of Yugoslavia and engaged in delaying efforts against German forces further south. In northern Serbia, the Soviet Red Army, with limited support from Bulgarian forces, assisted the Partisans in a joint liberation of the capital city of Belgrade on 20 October. A few days later, the Soviets launched a massive assault against German-occupied Hungary that lasted until the fall of Budapest in February 1945.[281] Unlike impressive Soviet victories in the Balkans, bitter Finnish resistance to the Soviet offensive in the Karelian Isthmus denied the Soviets occupation of Finland and led to a Soviet-Finnish armistice on relatively mild conditions,[282] although Finland was forced to fight their former German allies.[283]

By the start of July 1944, Commonwealth forces in Southeast Asia had repelled the Japanese sieges in Assam, pushing the Japanese back to the Chindwin River[284] while the Chinese captured Myitkyina. In September 1944, Chinese forces captured Mount Song and reopened the Burma Road.[285] In China, the Japanese had more successes, having finally captured Changsha in mid-June and the city of Hengyang by early August.[286] Soon after, they invaded the province of Guangxi, winning major engagements against Chinese forces at Guilin and Liuzhou by the end of November[287] and successfully linking up their forces in China and Indochina by mid-December.[288]

In the Pacific, US forces continued to push back the Japanese perimeter. In mid-June 1944, they began their offensive against the Mariana and Palau islands and decisively defeated Japanese forces in the Battle of the Philippine Sea. These defeats led to the resignation of the Japanese Prime Minister, Hideki Tojo, and provided the United States with air bases to launch intensive heavy bomber attacks on the Japanese home islands. In late October, American forces invaded the Filipino island of Leyte; soon after, Allied naval forces scored another large victory in the Battle of Leyte Gulf, one of the largest naval battles in history.[289]

Axis collapse and Allied victory (1944–1945)
Yalta Conference held in February 1945, with Winston Churchill, Franklin D. Roosevelt, and Joseph Stalin

On 16 December 1944, Germany made a last attempt to split the Allies on the Western Front by using most of its remaining reserves to launch a massive counter-offensive in the Ardennes and along the French-German border, hoping to encircle large portions of Western Allied troops and prompt a political settlement after capturing their primary supply port at Antwerp. By 16 January 1945, this offensive had been repulsed with no strategic objectives fulfilled.[290] In Italy, the Western Allies remained stalemated at the German defensive line. In mid-January 1945, the Red Army attacked in Poland, pushing from the Vistula to the Oder river in Germany, and overran East Prussia.[291] On 4 February Soviet, British, and US leaders met for the Yalta Conference. They agreed on the occupation of post-war Germany, and on when the Soviet Union would join the war against Japan.[292]

In February, the Soviets entered Silesia and Pomerania, while the Western Allies entered western Germany and closed to the Rhine river. By March, the Western Allies crossed the Rhine north and south of the Ruhr, encircling the German Army Group B.[293] In early March, in an attempt to protect its last oil reserves in Hungary and retake Budapest, Germany launched its last major offensive against Soviet troops near Lake Balaton. Within two weeks, the offensive had been repulsed, the Soviets advanced to Vienna, and captured the city. In early April, Soviet troops captured Königsberg, while the Western Allies finally pushed forward in Italy and swept across western Germany capturing Hamburg and Nuremberg. American and Soviet forces met at the Elbe river on 25 April, leaving unoccupied pockets in southern Germany and around Berlin.

Soviet troops stormed and captured Berlin in late April.[294] In Italy, German forces surrendered on 29 April, while the Italian Social Republic capitulated two days later. On 30 April, the Reichstag was captured, signalling the military defeat of Nazi Germany.[295]

Major changes in leadership occurred on both sides during this period. On 12 April, President Roosevelt died and was succeeded by his vice president, Harry S. Truman.[296] Benito Mussolini was killed by Italian partisans on 28 April.[297] On 30 April, Hitler committed suicide in his headquarters, and was succeeded by Grand Admiral Karl Dönitz (as President of the Reich) and Joseph Goebbels (as Chancellor of the Reich); Goebbels also committed suicide on the following day and was replaced by Lutz Graf Schwerin von Krosigk, in what would later be known as the Flensburg Government. Total and unconditional surrender in Europe was signed on 7 and 8 May, to be effective by the end of 8 May.[298] German Army Group Centre resisted in Prague until 11 May.[299] On 23 May all remaining members of the German government were arrested by the Allied Forces in Flensburg, while on 5 June all German political and military institutions were transferred under the control of the Allies through the Berlin Declaration.[300]

In the Pacific theatre, American forces accompanied by the forces of the Philippine Commonwealth advanced in the Philippines, clearing Leyte by the end of April 1945. They landed on Luzon in January 1945 and recaptured Manila in March. Fighting continued on Luzon, Mindanao, and other islands of the Philippines until the end of the war.[301] Meanwhile, the United States Army Air Forces launched a massive firebombing campaign of strategic cities in Japan in an effort to destroy Japanese war industry and civilian morale. A devastating bombing raid on Tokyo of 9–10 March was the deadliest conventional bombing raid in history.[302]

Japanese foreign affairs minister Mamoru Shigemitsu signs the Japanese Instrument of Surrender on board USS Missouri, 2 September 1945

In May 1945, Australian troops landed in Borneo, overrunning the oilfields there. British, American, and Chinese forces defeated the Japanese in northern Burma in March, and the British pushed on to reach Rangoon by 3 May.[303] Chinese forces started a counterattack in the Battle of West Hunan that occurred between 6 April and 7 June 1945. American naval and amphibious forces also moved towards Japan, taking Iwo Jima by March, and Okinawa by the end of June.[304] At the same time, a naval blockade by submarines was strangling Japan's economy and drastically reducing its ability to supply overseas forces.[305][306]

On 11 July, Allied leaders met in Potsdam, Germany. They confirmed earlier agreements about Germany,[307] and the American, British and Chinese governments reiterated the demand for unconditional surrender of Japan, specifically stating that "the alternative for Japan is prompt and utter destruction".[308] During this conference, the United Kingdom held its general election, and Clement Attlee replaced Churchill as Prime Minister.[309]

The call for unconditional surrender was rejected by the Japanese government, which believed it would be capable of negotiating for more favourable surrender terms.[310] In early August, the United States dropped atomic bombs on the Japanese cities of Hiroshima and Nagasaki. Between the two bombings, the Soviets, pursuant to the Yalta agreement, declared war on Japan, invaded Japanese-held Manchuria and quickly defeated the Kwantung Army, which was the largest Japanese fighting force.[311] These two events persuaded previously adamant Imperial Army leaders to accept surrender terms.[312] The Red Army also captured the southern part of Sakhalin Island and the Kuril Islands. On the night of 9–10 August 1945, Emperor Hirohito announced his decision to accept the terms demanded by the Allies in the Potsdam Declaration.[313] On 15 August, the Emperor communicated this decision to the Japanese people through a speech broadcast on the radio (Gyokuon-hōsō, literally "broadcast in the Emperor's voice").[314] On 15 August 1945, Japan surrendered, with the surrender documents finally signed at Tokyo Bay on the deck of the American battleship USS Missouri on 2 September 1945, ending the war.[315]

Aftermath
Main articles: Aftermath of World War II and Consequences of Nazism
Defendants at the Nuremberg trials, where the Allied forces prosecuted prominent members of the political, military, judicial, and economic leadership of Nazi Germany for crimes against humanity

The Allies established occupation administrations in Austria and Germany, both initially divided between western and eastern occupation zones controlled by the Western Allies and the Soviet Union, respectively. However, their paths soon diverged. In Germany, the western and eastern occupation zones controlled by the Western Allies and the Soviet Union officially ended in 1949, with the respective zones becoming separate countries, West Germany and East Germany.[316] In Austria, however, occupation continued until 1955, when a joint settlement between the Western Allies and the Soviet Union permitted the reunification of Austria as a democratic state officially non-aligned with any political bloc (although in practice having better relations with the Western Allies). A denazification program in Germany led to the prosecution of Nazi war criminals in the Nuremberg trials and the removal of ex-Nazis from power, although this policy moved towards amnesty and re-integration of ex-Nazis into West German society.[317]

Germany lost a quarter of its pre-war (1937) territory. Among the eastern territories, Silesia, Neumark and most of Pomerania were taken over by Poland,[318] and East Prussia was divided between Poland and the Soviet Union, followed by the expulsion to Germany of the nine million Germans from these provinces,[319][320] as well as three million Germans from the Sudetenland in Czechoslovakia. By the 1950s, one-fifth of West Germans were refugees from the east. The Soviet Union also took over the Polish provinces east of the Curzon Line,[321] from which two million Poles were expelled.[320][322] North-east Romania,[323][324] parts of eastern Finland,[325] and the Baltic states were annexed into the Soviet Union.[326][327] Italy lost its monarchy, colonial empire, and some European territories.[328]

In an effort to maintain world peace,[329] the Allies formed the United Nations,[330] which officially came into existence on 24 October 1945,[331] and adopted the Universal Declaration of Human Rights in 1948 as a common standard for all member nations.[332] The great powers that were the victors of the war—France, China, the United Kingdom, the Soviet Union, and the United States—became the permanent members of the UN's Security Council.[333] The five permanent members remain so to the present, although there have been two seat changes, between the Republic of China and the People's Republic of China in 1971, and between the Soviet Union and its successor state, the Russian Federation, following the dissolution of the Soviet Union in 1991. The alliance between the Western Allies and the Soviet Union had begun to deteriorate even before the war was over.[334]

Post-war border changes in Central Europe and creation of the Communist Eastern Bloc

Besides Germany, the rest of Europe was also divided into Western and Soviet spheres of influence.[335] Most eastern and central European countries fell into the Soviet sphere, which led to establishment of Communist-led regimes, with full or partial support of the Soviet occupation authorities. As a result, East Germany,[336] Poland, Hungary, Romania, Bulgaria, Czechoslovakia, and Albania[337] became Soviet satellite states. Communist Yugoslavia conducted a fully independent policy, causing tension with the Soviet Union.[338] A Communist uprising in Greece was put down with Anglo-American support and the country remained aligned with the West.[339]

Post-war division of the world was formalised by two international military alliances, the United States-led NATO and the Soviet-led Warsaw Pact.[340] The long period of political tensions and military competition between them—the Cold War—would be accompanied by an unprecedented arms race and number of proxy wars throughout the world.[341]

In Asia, the United States led the occupation of Japan and administered Japan's former islands in the Western Pacific, while the Soviets annexed South Sakhalin and the Kuril Islands.[342] Korea, formerly under Japanese colonial rule, was divided and occupied by the Soviet Union in the North and the United States in the South between 1945 and 1948. Separate republics emerged on both sides of the 38th parallel in 1948, each claiming to be the legitimate government for all of Korea, which led ultimately to the Korean War.[343]

In China, nationalist and communist forces resumed the civil war in June 1946. Communist forces were victorious and established the People's Republic of China on the mainland, while nationalist forces retreated to Taiwan in 1949.[344] In the Middle East, the Arab rejection of the United Nations Partition Plan for Palestine and the creation of Israel marked the escalation of the Arab–Israeli conflict. While European powers attempted to retain some or all of their colonial empires, their losses of prestige and resources during the war rendered this unsuccessful, leading to decolonisation.[345][346]

The global economy suffered heavily from the war, although participating nations were affected differently. The United States emerged much richer than any other nation, leading to a baby boom, and by 1950 its gross domestic product per person was much higher than that of any of the other powers, and it dominated the world economy.[347] The Allied occupational authorities pursued a policy of industrial disarmament in Western Germany from 1945 to 1948.[348] Due to international trade interdependencies, this policy led to an economic stagnation in Europe and delayed European recovery from the war for several years.[349][350]

At the Bretton Woods Conference in July 1944, the Allied nations drew up an economic framework for the post-war world. The agreement created the International Monetary Fund (IMF) and the International Bank for Reconstruction and Development (IBRD), which later became part of the World Bank Group. The Bretton Woods system lasted until 1973.[351] Recovery began with the mid-1948 currency reform in Western Germany, and was sped up by the liberalisation of European economic policy that the US Marshall Plan economic aid (1948–1951) both directly and indirectly caused.[352][353] The post-1948 West German recovery has been called the German economic miracle.[354] Italy also experienced an economic boom[355] and the French economy rebounded.[356] By contrast, the United Kingdom was in a state of economic ruin,[357] and although receiving a quarter of the total Marshall Plan assistance, more than any other European country,[358] it continued in relative economic decline for decades.[359] The Soviet Union, despite enormous human and material losses, also experienced rapid increase in production in the immediate post-war era,[360] having seized and transferred most of Germany's industrial plants and exacted war reparations from its satellite states.[d][361] Japan recovered much later.[362] China returned to its pre-war industrial production by 1952.[363]

Impact
Main article: Historiography of World War II
Casualties and war crimes
Main article: World War II casualties
Further information: War crimes in World War II
World War II deaths

Estimates for the total number of casualties in the war vary, because many deaths went unrecorded.[364] Most suggest 60 million people died, about 20 million military personnel and 40 million civilians.[365][366]

The Soviet Union alone lost around 27 million people during the war,[367] including 8.7 million military and 19 million civilian deaths.[368] A quarter of the total people in the Soviet Union were wounded or killed.[369] Germany sustained 5.3 million military losses, mostly on the Eastern Front and during the final battles in Germany.[370]

An estimated 11[371] to 17 million[372] civilians died as a direct or as an indirect result of Hitler's racist policies, including mass killing of around 6 million Jews, along with Roma, homosexuals, at least 1.9 million ethnic Poles[373][374] and millions of other Slavs (including Russians, Ukrainians and Belarusians), and other ethnic and minority groups.[375][372] Between 1941 and 1945, more than 200,000 ethnic Serbs, along with Roma and Jews, were persecuted and murdered by the Axis-aligned Croatian Ustaše in Yugoslavia.[376] Concurrently, Muslims and Croats were persecuted and killed by Serb nationalist Chetniks,[377] with an estimated 50,000–68,000 victims (of which 41,000 were civilians).[378] Also, more than 100,000 Poles were massacred by the Ukrainian Insurgent Army in the Volhynia massacres, between 1943 and 1945.[379] At the same time, about 10,000–15,000 Ukrainians were killed by the Polish Home Army and other Polish units, in reprisal attacks.[380]

Bodies of Chinese civilians killed by the Imperial Japanese Army during the Nanjing Massacre in December 1937

In Asia and the Pacific, the number of people killed by Japanese troops remains contested. According to R.J. Rummel, the Japanese killed between 3 million and more than 10 million people, with the most probable case of almost 6,000,000 people.[381] According to the British historian M. R. D. Foot, civilian deaths are between 10 million and 20 million, whereas Chinese military casualties (killed and wounded) are estimated to be over five million.[382] Other estimates say that up to 30 million people, most of them civilians, were killed.[383][384] The most infamous Japanese atrocity was the Nanjing Massacre, in which fifty to three hundred thousand Chinese civilians were raped and murdered.[385] Mitsuyoshi Himeta reported that 2.7 million casualties occurred during the Three Alls policy. General Yasuji Okamura implemented the policy in Hebei and Shandong.[386]

Axis forces employed biological and chemical weapons. The Imperial Japanese Army used a variety of such weapons during its invasion and occupation of China (see Unit 731)[387][388] and in early conflicts against the Soviets.[389] Both the Germans and the Japanese tested such weapons against civilians,[390] and sometimes on prisoners of war.[391]

The Soviet Union was responsible for the Katyn massacre of 22,000 Polish officers,[392] and the imprisonment or execution of hundreds of thousands of political prisoners by the NKVD secret police, along with mass civilian deportations to Siberia, in the Baltic states and eastern Poland annexed by the Red Army.[393] Soviet soldiers committed mass rapes in occupied territories, especially in Germany.[394][395] The exact number of German women and girls raped by Soviet troops during the war and occupation is uncertain, but historians estimate their numbers are likely in the hundreds of thousands, and possibly as many as two million,[396] while figures for women raped by German soldiers in the Soviet Union go as far as ten million.[397][398]

The mass bombing of cities in Europe and Asia has often been called a war crime, although no positive or specific customary international humanitarian law with respect to aerial warfare existed before or during World War II.[399] The USAAF bombed a total of 67 Japanese cities, killing 393,000 civilians, including the atomic bombings of Hiroshima and Nagasaki, and destroying 65% of built-up areas.[400]

Genocide, concentration camps, and slave labour
Main articles: The Holocaust, Nazi concentration camps, Extermination camp, Forced labour under German rule during World War II, Kidnapping of children by Nazi Germany, Nazi human experimentation, Soviet war crimes § World War II, and Japanese war crimes
Schutzstaffel (SS) female camp guards removing prisoners' bodies from lorries and carrying them to a mass grave, inside the German Bergen-Belsen concentration camp, 1945

Nazi Germany, under the dictatorship of Adolf Hitler, was responsible for murdering about 6 million Jews in what is now known as the Holocaust. They also murdered an additional 4 million others who were deemed "unworthy of life" (including the disabled and mentally ill, Soviet prisoners of war, Romani, homosexuals, Freemasons, and Jehovah's Witnesses) as part of a program of deliberate extermination, in effect becoming a "genocidal state".[401] Soviet POWs were kept in especially unbearable conditions, and 3.6 million Soviet POWs out of 5.7 million died in Nazi camps during the war.[402][403] In addition to concentration camps, death camps were created in Nazi Germany to exterminate people on an industrial scale. Nazi Germany extensively used forced labourers; about 12 million Europeans from German-occupied countries were abducted and used as a slave work force in German industry, agriculture and war economy.[404]

Prisoner identity photograph of a Polish girl taken by the German SS in Auschwitz.[405] Approximately 230,000 children were held prisoner and used in forced labour and Nazi medical experiments

The Soviet Gulag became a de facto system of deadly camps during 1942–1943, when wartime privation and hunger caused numerous deaths of inmates,[406] including foreign citizens of Poland and other countries occupied in 1939–1940 by the Soviet Union, as well as Axis POWs.[407] By the end of the war, most Soviet POWs liberated from Nazi camps and many repatriated civilians were detained in special filtration camps where they were subjected to NKVD evaluation, and 226,127 were sent to the Gulag as real or perceived Nazi collaborators.[408]

Japanese prisoner-of-war camps, many of which were used as labour camps, also had high death rates. The International Military Tribunal for the Far East found the death rate of Western prisoners was 27 percent (for American POWs, 37 percent),[409] seven times that of POWs under the Germans and Italians.[410] While 37,583 prisoners from the UK, 28,500 from the Netherlands, and 14,473 from the United States were released after the surrender of Japan, the number of Chinese released was only 56.[411]

At least five million Chinese civilians from northern China and Manchukuo were enslaved between 1935 and 1941 by the East Asia Development Board, or Kōain, for work in mines and war industries. After 1942, the number reached 10 million.[412] In Java, between 4 and 10 million rōmusha (Japanese: "manual labourers"), were forced to work by the Japanese military. About 270,000 of these Javanese labourers were sent to other Japanese-held areas in Southeast Asia, and only 52,000 were repatriated to Java.[413]

Occupation
Main articles: German-occupied Europe, Resistance during World War II, Collaboration with Nazi Germany and Fascist Italy, Collaboration with Imperial Japan, and Nazi plunder
Polish civilians wearing blindfolds photographed just before being massacred by German soldiers in Palmiry forest, 1940

In Europe, occupation came under two forms. In Western, Northern, and Central Europe (France, Norway, Denmark, the Low Countries, and the annexed portions of Czechoslovakia) Germany established economic policies through which it collected roughly 69.5 billion reichsmarks (27.8 billion US dollars) by the end of the war; this figure does not include the plunder of industrial products, military equipment, raw materials and other goods.[414] Thus, the income from occupied nations was over 40 percent of the income Germany collected from taxation, a figure which increased to nearly 40 percent of total German income as the war went on.[415]

Soviet partisans hanged by the German army. The Russian Academy of Sciences reported in 1995 that civilian victims in the Soviet Union at German hands totalled 13.7 million dead, twenty percent of the 68 million people in the occupied Soviet Union

In the East, the intended gains of Lebensraum were never attained as fluctuating front-lines and Soviet scorched earth policies denied resources to the German invaders.[416] Unlike in the West, the Nazi racial policy encouraged extreme brutality against what it considered to be the "inferior people" of Slavic descent; most German advances were thus followed by mass atrocities and war crimes.[417] The Nazis killed an estimated 2.8 million ethnic Poles in addition to Polish-Jewish victims of the Holocaust.[418] Although resistance groups formed in most occupied territories, they did not significantly hamper German operations in either the East[419] or the West[420] until late 1943.

In Asia, Japan termed nations under its occupation as being part of the Greater East Asia Co-Prosperity Sphere, essentially a Japanese hegemony which it claimed was for purposes of liberating colonised peoples.[421] Although Japanese forces were sometimes welcomed as liberators from European domination, Japanese war crimes frequently turned local public opinion against them.[422] During Japan's initial conquest, it captured 4,000,000 barrels (640,000 m3) of oil (~550,000 tonnes) left behind by retreating Allied forces; and by 1943, was able to get production in the Dutch East Indies up to 50 million barrels (7,900,000 m3) of oil (~6.8 million tonnes), 76 percent of its 1940 output rate.[422]

Home fronts and production
Main articles: Military production during World War II and Home front during World War II
Allies to Axis GDP ratio throughout the war

In the 1930s Britain and the United States together controlled almost 75% of world mineral output—essential for projecting military power.[423]

In Europe, before the outbreak of the war, the Allies had significant advantages in both population and economics. In 1938, the Western Allies (United Kingdom, France, Poland and the British Dominions) had a 30 percent larger population and a 30 percent higher gross domestic product than the European Axis powers (Germany and Italy); including colonies, the Allies had more than a 5:1 advantage in population and a nearly 2:1 advantage in GDP.[424] In Asia at the same time, China had roughly six times the population of Japan but only an 89 percent higher GDP; this reduces to three times the population and only a 38 percent higher GDP if Japanese colonies are included.[424]

The United States produced about two-thirds of all munitions used by the Allies in World War II, including warships, transports, warplanes, artillery, tanks, trucks, and ammunition.[425] Although the Allies' economic and population advantages were largely mitigated during the initial rapid blitzkrieg attacks of Germany and Japan, they became the decisive factor by 1942, after the United States and Soviet Union joined the Allies and the war evolved into one of attrition.[426] While the Allies' ability to out-produce the Axis was partly due to more access to natural resources, other factors, such as Germany and Japan's reluctance to employ women in the labour force,[427] Allied strategic bombing,[428] and Germany's late shift to a war economy[429] contributed significantly. Additionally, neither Germany nor Japan planned to fight a protracted war, and had not equipped themselves to do so.[430] To improve their production, Germany and Japan used millions of slave labourers;[431] Germany enslaved about 12 million people, mostly from Eastern Europe,[404] while Japan used more than 18 million people in Far East Asia.[412][413]

Advances in technology and its application
Main article: Technology during World War II
A V-2 rocket launched from a fixed site in Peenemünde, 21 June 1943

Aircraft were used for reconnaissance, as fighters, bombers, and ground-support, and each role developed considerably. Innovations included airlift (the capability to quickly move limited high-priority supplies, equipment, and personnel);[432] and strategic bombing (the bombing of enemy industrial and population centres to destroy the enemy's ability to wage war).[433] Anti-aircraft weaponry also advanced, including defences such as radar and surface-to-air artillery, in particular the introduction of the proximity fuze. The use of the jet aircraft was pioneered and led to jets becoming standard in air forces worldwide.[434]

Advances were made in nearly every aspect of naval warfare, most notably with aircraft carriers and submarines. Although aeronautical warfare had relatively little success at the start of the war, actions at Taranto, Pearl Harbor, and the Coral Sea established the carrier as the dominant capital ship (in place of the battleship).[435][436][437] In the Atlantic, escort carriers became a vital part of Allied convoys, increasing the effective protection radius and helping to close the Mid-Atlantic gap.[438] Carriers were also more economical than battleships due to the relatively low cost of aircraft[439] and because they are not required to be as heavily armoured.[440] Submarines, which had proved to be an effective weapon during the First World War,[441] were expected by all combatants to be important in the second. The British focused development on anti-submarine weaponry and tactics, such as sonar and convoys, while Germany focused on improving its offensive capability, with designs such as the Type VII submarine and wolfpack tactics.[442] Gradually, improving Allied technologies such as the Leigh Light, Hedgehog, Squid, and homing torpedoes proved effective against German submarines.[443]

Nuclear Gadget being raised to the top of the detonation "shot tower", at Alamogordo Bombing Range; Trinity nuclear test, New Mexico, July 1945

Land warfare changed from the static frontlines of trench warfare of World War I, which had relied on improved artillery that outmatched the speed of both infantry and cavalry, to increased mobility and combined arms. The tank, which had been used predominantly for infantry support in the First World War, had evolved into the primary weapon.[444] In the late 1930s, tank design was considerably more advanced than it had been during World War I,[445] and advances continued throughout the war with increases in speed, armour and firepower.[446][447] At the start of the war, most commanders thought enemy tanks should be met by tanks with superior specifications.[448] This idea was challenged by the poor performance of the relatively light early tank guns against armour, and German doctrine of avoiding tank-versus-tank combat. This, along with Germany's use of combined arms, were among the key elements of their highly successful blitzkrieg tactics across Poland and France.[444] Many means of destroying tanks, including indirect artillery, anti-tank guns (both towed and self-propelled), mines, short-ranged infantry antitank weapons, and other tanks were used.[448] Even with large-scale mechanisation, infantry remained the backbone of all forces,[449] and throughout the war, most infantry were equipped similarly to World War I.[450] The portable machine gun spread, a notable example being the German MG 34, and various submachine guns which were suited to close combat in urban and jungle settings.[450] The assault rifle, a late war development incorporating many features of the rifle and submachine gun, became the standard post-war infantry weapon for most armed forces.[451]

Most major belligerents attempted to solve the problems of complexity and security involved in using large codebooks for cryptography by designing ciphering machines, the most well-known being the German Enigma machine.[452] Development of SIGINT (signals intelligence) and cryptanalysis enabled the countering process of decryption. Notable examples were the Allied decryption of Japanese naval codes[453] and British Ultra, a pioneering method for decoding Enigma that benefited from information given to the United Kingdom by the Polish Cipher Bureau, which had been decoding early versions of Enigma before the war.[454] Another component of military intelligence was deception, which the Allies used to great effect in operations such as Mincemeat and Bodyguard.[453][455]

Other technological and engineering feats achieved during, or as a result of, the war include the world's first programmable computers (Z3, Colossus, and ENIAC), guided missiles and modern rockets, the Manhattan Project's development of nuclear weapons, operations research, the development of artificial harbours, and oil pipelines under the English Channel.[456] Penicillin was first developed, mass-produced, and used during the war.[457]

See also
Opposition to World War II
World War III
Notes
^ While various other dates have been proposed as the date on which World War II began or ended, this is the period most frequently cited.
^ Often abbreviated as WWII or WW2
^ The UK declared war on Germany at 11 am. France followed 6 hours later at 5 pm.
^ Reparations were exacted from East Germany, Hungary, Romania, and Bulgaria using Soviet-dominated joint enterprises. The Soviet Union also instituted trading arrangements deliberately designed to favour the country. Moscow controlled the Communist parties that ruled the satellite states, and they followed orders from the Kremlin. Historian Mark Kramer concludes: "The net outflow of resources from eastern Europe to the Soviet Union was approximately $15 billion to $20 billion in the first decade after World War II, an amount roughly equal to the total aid provided by the United States to western Europe under the Marshall Plan."
References
See also: Bibliography of World War II
^ Weinberg 2005, p. 6.
^ Wells, Anne Sharp (2014) Historical Dictionary of World War II: The War against Germany and Italy. Rowman & Littlefield. p. 7.
^ Ferris, John; Mawdsley, Evan (2015). The Cambridge History of the Second World War, Volume I: Fighting the War. Cambridge: Cambridge University Press.
^ Förster & Gessler 2005, p. 64.
^ Ghuhl, Wernar (2007) Imperial Japan's World War Two Transaction Publishers pp. 7, 30
^ Polmar, Norman; Thomas B. Allen (1991) World War II: America at war, 1941–1945 ISBN 978-0-3945-8530-7
^ Hett, Benjamin Carter (1 August 1996). "'Goak here': A.J.P. Taylor and 'The Origins of the Second World War.'". Canadian Journal of History. 31 (2): 257–281. doi:10.3138/cjh.31.2.257. ISSN 0008-4107. Archived from the original on 7 March 2023. Retrieved 14 September 2022.
^ Ben-Horin 1943, p. 169; Taylor 1979, p. 124; Yisreelit, Hevrah Mizrahit (1965). Asian and African Studies, p. 191.
For 1941 see Taylor 1961, p. vii; Kellogg, William O (2003). American History the Easy Way. Barron's Educational Series. p. 236 ISBN 978-0-7641-1973-6.
There is also the viewpoint that both World War I and World War II are part of the same "European Civil War" or "Second Thirty Years' War": Canfora 2006, p. 155; Prins 2002, p. 11.
^ Beevor 2012, p. 10.
^ "In Many Ways, Author Says, Spanish Civil War Was 'The First Battle Of WWII'". Fresh Air. NPR. 10 March 2017. Archived from the original on 16 April 2021. Retrieved 16 April 2021.
^ Frank, Willard C. (1987). "The Spanish Civil War and the Coming of the Second World War". The International History Review. 9 (3): 368–409. doi:10.1080/07075332.1987.9640449. JSTOR 40105814. Archived from the original on 1 February 2022. Retrieved 17 February 2022.
^ Masaya 1990, p. 4.
^ "German-American Relations – Treaty on the Final Settlement concerning Germany". usa.usembassy.de. 12 September 1990. Archived from the original on 7 May 2012. Retrieved 6 May 2012.
^ Why Japan and Russia never signed a WWII peace treaty Archived 4 June 2018 at the Wayback Machine. Asia Times.
^ Texts of Soviet–Japanese Statements; Peace Declaration Trade Protocol. Archived 9 December 2021 at the Wayback Machine The New York Times, page 2, 20 October 1956.
Subtitle: "Moscow, October 19. (UP) – Following are the texts of a Soviet–Japanese peace declaration and of a trade protocol between the two countries, signed here today, in unofficial translation from the Russian". Quote: "The state of war between the USSR and Japan ends on the day the present declaration enters into force [...]"
^ Mintz, Steven. "Historical Context: The Global Effect of World War I". The Gilder Lehrman Institute of American History. Archived from the original on 4 March 2024. Retrieved 4 March 2024.
^ Gerwarth, Robert. "Paris Peace Treaties failed to create a secure, peaceful and lasting world order". The Irish Times. Archived from the original on 14 August 2021. Retrieved 29 October 2021.
^ Ingram 2006, pp. 76–78.
^ Kantowicz 1999, p. 149.
^ Shaw 2000, p. 35.
^ Brody 1999, p. 4.
^ Zalampas 1989, p. 62.
^ Mandelbaum 1988, p. 96; Record 2005, p. 50.
^ Schmitz 2000, p. 124.
^ Adamthwaite 1992, p. 52.
^ Shirer 1990, pp. 298–299.
^ Preston 1998, p. 104.
^ Myers & Peattie 1987, p. 458.
^ Smith & Steadman 2004, p. 28.
^ Coogan 1993: "Although some Chinese troops in the Northeast managed to retreat south, others were trapped by the advancing Japanese Army and were faced with the choice of resistance in defiance of orders, or surrender. A few commanders submitted, receiving high office in the puppet government, but others took up arms against the invader. The forces they commanded were the first of the volunteer armies."
^ Busky 2002, p. 10.
^ Stanton, Andrea L.; Ramsamy, Edward; Seybolt, Peter J. (2012). Cultural Sociology of the Middle East, Asia, and Africa: An Encyclopedia. p. 308. ISBN 978-1-4129-8176-7. Archived from the original on 7 March 2023. Retrieved 6 April 2014.
^ Barker 1971, pp. 131–132.
^ Shirer 1990, p. 289.
^ Kitson 2001, p. 231.
^ Neulen 2000, p. 25.
^ Payne 2008, p. 271.
^ Payne 2008, p. 146.
^ Eastman 1986, pp. 547–551.
^ Hsu & Chang 1971, pp. 195–200.
^ Tucker, Spencer C. (2009). A Global Chronology of Conflict: From the Ancient World to the Modern Middle East [6 volumes]: From the Ancient World to the Modern Middle East. ABC-CLIO. ISBN 978-1-8510-9672-5. Archived from the original on 7 March 2023. Retrieved 27 August 2017 – via Google Books.
^ Yang Kuisong, "On the reconstruction of the facts of the Battle of Pingxingguan"
^ Levene, Mark and Roberts, Penny. The Massacre in History. 1999, pp. 223–224
^ Totten, Samuel. Dictionary of Genocide. 2008, 298–299.
^ Hsu & Chang 1971, pp. 221–230.
^ Eastman 1986, p. 566.
^ Taylor 2009, pp. 150–152.
^ Sella 1983, pp. 651–687.
^ Beevor 2012, p. 342.
^ Goldman, Stuart D. (28 August 2012). "The Forgotten Soviet-Japanese War of 1939". The Diplomat. Archived from the original on 29 June 2015. Retrieved 26 June 2015.
^ Neeno, Timothy. "Nomonhan: The Second Russo-Japanese War". MilitaryHistoryOnline.com. Archived from the original on 24 November 2005. Retrieved 26 June 2015.
^ Collier & Pedley 2000, p. 144.
^ Kershaw 2001, pp. 121–122.
^ Kershaw 2001, p. 157.
^ Davies 2006, pp. 143–144 (2008 ed.).
^ Shirer 1990, pp. 461–462.
^ Lowe & Marzari 2002, p. 330.
^ Dear & Foot 2001, p. 234.
^ Shirer 1990, p. 471.
^ Shore 2003, p. 108.
^ Watson, Derek (2000). "Molotov's Apprenticeship in Foreign Policy: The Triple Alliance Negotiations in 1939". Europe-Asia Studies. 52 (4): 695–722. doi:10.1080/713663077. JSTOR 153322. S2CID 144385167.
^ Dear & Foot 2001, p. 608.
^ "The German Campaign In Poland (1939)". Archived from the original on 24 May 2014. Retrieved 29 October 2014.
^ 
Jump up to:
a b "The Danzig Crisis". ww2db.com. Archived from the original on 5 May 2016. Retrieved 29 April 2016.
^ 
Jump up to:
a b "Major international events of 1939, with explanation". Ibiblio.org. Archived from the original on 10 March 2013. Retrieved 9 May 2013.
^ "Historyczna fotografia było pozowaną "ustawką"!". PolskieRadio.pl (in Polish). Retrieved 18 March 2025.
^ Evans 2008, pp. 1–2.
^ Zabecki, David T. (2015). World War II in Europe: An Encyclopedia. Routledge. p. 1663. ISBN 978-1-1358-1242-3. Archived from the original on 7 March 2023. Retrieved 17 June 2019. The earliest fighting started at 0445 hours when marines from the battleship Schleswig-Holstein attempted to storm a small Polish fort in Danzig, the Westerplate
^ Keegan 1997, p. 35.
Cienciala 2010, p. 128, observes that, while it is true that Poland was far away, making it difficult for the French and British to provide support, "[f]ew Western historians of World War II ... know that the British had committed to bomb Germany if it attacked Poland, but did not do so except for one raid on the base of Wilhelmshaven. The French, who committed to attacking Germany in the west, had no intention of doing so."
^ Beevor 2012, p. 32; Dear & Foot 2001, pp. 248–249; Roskill 1954, p. 64.
^ "Battle of the Atlantic". Sky HISTORY TV channel. Archived from the original on 20 May 2022. Retrieved 11 July 2022.
^ Zaloga 2002, pp. 80, 83.
^ Ginsburgs, George (1958). "A Case Study in the Soviet Use of International Law: Eastern Poland in 1939". The American Journal of International Law. 52 (1): 69–84. doi:10.2307/2195670. JSTOR 2195670. S2CID 146904066.
^ Hempel 2005, p. 24.
^ Zaloga 2002, pp. 88–89.
^ Nuremberg Documents C-62/GB86, a directive from Hitler in October 1939 which concludes: "The attack [on France] is to be launched this Autumn if conditions are at all possible."
^ Liddell Hart 1977, pp. 39–40.
^ Bullock 1990, pp. 563–564, 566, 568–569, 574–575 (1983 ed.).
^ Deighton, Len (1979). Blitzkrieg: From the Rise of Hitler to the Fall of Dunkirk. Jonathan Cape. pp. 186–187. ISBN 978-0-2240-1648-3. Deighton states that "the offensive was postponed twenty-nine times before it finally took place."
^ Smith et al. 2002, p. 24.
^ 
Jump up to:
a b Bilinsky 1999, p. 9.
^ Murray & Millett 2001, pp. 55–56.
^ Spring 1986, pp. 207–226.
^ van Dyke, Carl (1997). The Soviet Invasion of Finland. Portland, Oregon: Frank Cass Publishers. p. 71. ISBN 978-0-7146-4753-1.
^ Hanhimäki 1997, p. 12.
^ Dear & Foot 2001, pp. 745, 975.
^ Haynes, Rebecca (2000). Romanian policy towards Germany, 1936–40. Palgrave Macmillan. p. 205. ISBN 978-0-3122-3260-3. Archived from the original on 7 March 2023. Retrieved 3 February 2022.
^ Deletant, pp. 48–51, 66; Griffin (1993), p. 126; Ornea, pp. 325–327
^ Ferguson 2006, pp. 367, 376, 379, 417.
^ Snyder 2010, pp. 118ff.
^ Koch 1983, pp. 912–914, 917–920.
^ Roberts 2006, p. 56.
^ Roberts 2006, p. 59.
^ Murray & Millett 2001, pp. 57–63.
^ Commager 2004, p. 9.
^ Reynolds 2006, p. 76.
^ Evans 2008, pp. 122–123.
^ Keegan 1997, pp. 59–60.
^ Regan 2004, p. 152.
^ Liddell Hart 1977, p. 48.
^ Keegan 1997, pp. 66–67.
^ Overy & Wheatcroft 1999, p. 207.
^ Umbreit 1991, p. 311.
^ Brown 2004, p. 198.
^ Keegan 1997, p. 72.
^ 
Jump up to:
a b Murray 1983, The Battle of Britain.
^ Dear & Foot 2001, pp. 108–109.
^ Goldstein 2004, p. 35
^ Steury 1987, p. 209; Zetterling & Tamelander 2009, p. 282.
^ Overy & Wheatcroft 1999, pp. 328–330.
^ Maingot 1994, p. 52.
^ Cantril 1940, p. 390.
^ 
Jump up to:
a b "Major international events of 1940, with explanation". Ibiblio.org. Archived from the original on 25 May 2013.
^ Skinner Watson, Mark. "Coordination With Britain". US Army in WWII – Chief of Staff: Prewar Plans and Operations. Archived from the original on 30 April 2013. Retrieved 13 May 2013.
^ Bilhartz & Elliott 2007, p. 179.
^ Dear & Foot 2001, p. 877.
^ Dear & Foot 2001, pp. 745–746.
^ Clogg 2002, p. 118.
^ Evans 2008, pp. 146, 152; US Army 1986, pp. 4–6
^ Jowett 2001, pp. 9–10.
^ Jackson 2006, p. 106.
^ Laurier 2001, pp. 7–8.
^ Murray & Millett 2001, pp. 263–276.
^ Gilbert 1989, pp. 174–175.
^ Gilbert 1989, pp. 184–187.
^ Gilbert 1989, pp. 208, 575, 604.
^ Watson 2003, p. 80.
^ Morrisey, Will (2019). "What Churchill and De Gaulle learned from the Great War". Winston Churchill. Routledge. pp. 119–126. doi:10.4324/9780429027642-6. ISBN 978-0-4290-2764-2. S2CID 189257503.
^ Garver 1988, p. 114.
^ Weinberg 2005, p. 195.
^ Murray 1983, p. 69.
^ Förster 1998, p. 26.
^ Förster 1998, pp. 38–42.
^ Shirer 1990, pp. 810–812.
^ 
Jump up to:
a b Klooz, Marle; Wiley, Evelyn (1944). Events leading up to World War II – Chronological History. 78th Congress, 2d Session – House Document N. 541. Director: Humphrey, Richard A. Washington, DC: US Government Printing Office. pp. 267–312 (1941). Archived from the original on 14 December 2013. Retrieved 9 May 2013.
^ Sella 1978, p. 555.
^ Kershaw 2007, pp. 66–69.
^ Steinberg 1995.
^ Hauner 1978.
^ Roberts 1995.
^ Wilt 1981.
^ Erickson 2003, pp. 114–137.
^ Glantz 2001, p. 9.
^ Farrell 1993.
^ Keeble 1990, p. 29.
^ Beevor 2012, p. 220.
^ Bueno de Mesquita et al. 2003, p. 425.
^ Kleinfeld 1983.
^ Jukes 2001, p. 113.
^ Glantz 2001, p. 26: "By 1 November [the Wehrmacht] had lost fully 20% of its committed strength (686,000 men), up to 2/3 of its ½ million motor vehicles, and 65 percent of its tanks. The German Army High Command (OKH) rated its 136 divisions as equivalent to 83 full-strength divisions."
^ Reinhardt 1992, p. 227.
^ Milward 1964.
^ Rotundo 1986.
^ Glantz 2001, p. 26.
^ Deighton, Len (1993). Blood, Tears and Folly. London: Pimlico. p. 479. ISBN 978-0-7126-6226-0.
^ Beevor 1998, pp. 41–42; Evans 2008, pp. 213–214, notes that "Zhukov had pushed the Germans back where they had launched Operation Typhoon two months before. ... Only Stalin's decision to attack all along the front instead of concentrating his forces in an all-out assault against the retreating German Army Group Centre prevented the disaster from being even worse."
^ "Peace and War: United States Foreign Policy, 1931–1941". U.S. Department of State Publication (1983): 87–97. 1983. Archived from the original on 14 January 2022. Retrieved 17 February 2022.
^ Maechling, Charles. Pearl Harbor: The First Energy War. History Today. December 2000
^ Jowett & Andrew 2002, p. 14.
^ Overy & Wheatcroft 1999, p. 289.
^ Frank 2020, p. 161.
^ Joes 2004, p. 224.
^ Fairbank & Goldman 2006, p. 320.
^ Hsu & Chang 1971, p. 30.
^ Hsu & Chang 1971, p. 33.
^ "Japanese Policy and Strategy 1931 – July 1941". US Army in WWII – Strategy and Command: The First Two Years. pp. 45–66. Archived from the original on 6 January 2013. Retrieved 15 May 2013.
^ Anderson 1975, p. 201.
^ Evans & Peattie 2012, p. 456.
^ Coox, Alvin (1985). Nomonhan: Japan against Russia, 1939. Stanford, California: Stanford University Press. pp. 1046–1049. ISBN 978-0-8047-1835-6.
^ 
Jump up to:
a b "The decision for War". US Army in WWII – Strategy, and Command: The First Two Years. pp. 113–127. Archived from the original on 25 May 2013. Retrieved 15 May 2013.
^ 
Jump up to:
a b "The Showdown With Japan Aug–Dec 1941". US Army in WWII – Strategic Planning for Coalition Warfare. pp. 63–96. Archived from the original on 9 November 2012. Retrieved 15 May 2013.
^ Bix 2000, pp. 399–414.
^ Kitano, Ryuichi (6 December 2021). "Diary: Hirohito prepared for U.S. war before Pearl Harbor attack". The Asahi Shimbun. Archived from the original on 17 April 2022. Retrieved 8 June 2022.
^ Fujiwara, Akira (1991). Shōwa tennō no jūgo-nen sensō. p. 126, citing Kenji Tomita's diary.
^ Bix 2000, pp. 417–420.
^ Bix 2000, p. 418.
^ Wetzler, Peter (1998). Hirohito and War: Imperial Tradition and Military Decision Making in Prewar Japan. University of Hawai'i Press. pp. 29, 35. ISBN 978-0-8248-1925-5. Archived from the original on 15 March 2024. Retrieved 15 January 2024.
^ Bix 2000, p. 424.
^ The United States Replies Archived 29 April 2013 at the Wayback Machine. Investigation of the Pearl Harbor attack.
^ Painter 2012, p. 26: "The United States cut off oil exports to Japan in the summer of 1941, forcing Japanese leaders to choose between going to war to seize the oil fields of the Netherlands East Indies or giving in to US pressure."
^ Wood 2007, p. 9, listing various military and diplomatic developments, observes that "the threat to Japan was not purely economic."
^ Lightbody 2004, p. 125.
^ Weinberg 2005, p. 310
^ Dower 1986, p. 5, calls attention to the fact that "the Allied struggle against Japan exposed the racist underpinnings of the European and American colonial structure. Japan did not invade independent countries in southern Asia. It invaded colonial outposts which the Westerners had dominated for generations, taking absolutely for granted their racial and cultural superiority over their Asian subjects." Dower goes on to note that, before the horrors of Japanese occupation made themselves felt, many Asians responded favourably to the victories of the Imperial Japanese forces.
^ Wood 2007, pp. 11–12.
^ 
Jump up to:
a b Wohlstetter 1962, pp. 341–343.
^ Keegan, John (1989) The Second World War. New York: Viking. pp. 256–257. ISBN 978-0-3995-0434-1
^ Dunn 1998, p. 157. According to May 1955, p. 155, Churchill stated: "Russian declaration of war on Japan would be greatly to our advantage, provided, but only provided, that Russians are confident that will not impair their Western Front."
^ Adolf Hitler's Declaration of War against the United States in Wikisource.
^ Klooz, Marle; Wiley, Evelyn (1944). Events leading up to World War II – Chronological History. 78th Congress, 2d Session – House Document N. 541. Director: Humphrey, Richard A. Washington, DC: US Government Printing Office. p. 310 (1941). Archived from the original on 14 December 2013. Retrieved 9 May 2013.
^ Bosworth & Maiolo 2015, pp. 313–314.
^ Mingst & Karns 2007, p. 22.
^ Shirer 1990, p. 904.
^ "The First Full Dress Debate over Strategic Deployment. Dec 1941 – Jan 1942". US Army in WWII – Strategic Planning for Coalition Warfare. pp. 97–119. Archived from the original on 9 November 2012. Retrieved 16 May 2013.
^ "The Elimination of the Alternatives. Jul–Aug 1942". US Army in WWII – Strategic Planning for Coalition Warfare. pp. 266–292. Archived from the original on 30 April 2013. Retrieved 16 May 2013.
^ "Casablanca – Beginning of an Era: January 1943". US Army in WWII – Strategic Planning for Coalition Warfare. pp. 18–42. Archived from the original on 25 May 2013. Retrieved 16 May 2013.
^ "The Trident Conference – New Patterns: May 1943". US Army in WWII – Strategic Planning for Coalition Warfare. pp. 126–145. Archived from the original on 25 May 2013. Retrieved 16 May 2013.
^ Beevor 2012, pp. 247–267, 345.
^ Lewis 1953, p. 529 (Table 11).
^ Slim 1956, pp. 71–74.
^ Grove 1995, p. 362.
^ Ch'i 1992, p. 158.
^ Perez 1998, p. 145.
^ Maddox 1992, pp. 111–112.
^ Salecker 2001, p. 186.
^ Schoppa 2011, p. 28.
^ Chevrier & Chomiczewski & Garrigue 2004, p. 19.
^ Ropp 2000, p. 368.
^ Weinberg 2005, p. 339.
^ Gilbert, Adrian (2003). The Encyclopedia of Warfare: From Earliest Times to the Present Day. Globe Pequot. p. 259. ISBN 978-1-5922-8027-8. Archived from the original on 19 July 2019. Retrieved 26 June 2019.
^ Swain 2001, p. 197.
^ Hane 2001, p. 340.
^ Marston 2005, p. 111.
^ Brayley 2002, p. 9.
^ Glantz 2001, p. 31.
^ Read 2004, p. 764.
^ Davies 2006, p. 100 (2008 ed.).
^ Beevor 1998, pp. 239–265.
^ Black 2003, p. 119.
^ Beevor 1998, pp. 383–391.
^ Erickson 2001, p. 142.
^ Milner 1990, p. 52.
^ Beevor 2012, pp. 224–228.
^ Molinari 2007, p. 91.
^ Mitcham 2007, p. 31.
^ Beevor 2012, pp. 380–381.
^ Rich 1992, p. 178.
^ Gordon 2004, p. 129.
^ Neillands 2005, p. 60.
^ Keegan 1997, p. 277.
^ Smith 2002.
^ Thomas & Andrew 1998, p. 8.
^ 
Jump up to:
a b c d Ross 1997, p. 38.
^ Bonner & Bonner 2001, p. 24.
^ Collier 2003, p. 11.
^ "The Civilians" Archived 5 November 2013 at the Wayback Machine the United States Strategic Bombing Survey Summary Report (European War)
^ Overy 1995, pp. 119–120.
^ Thompson & Randall 2008, p. 164.
^ Kennedy 2001, p. 610.
^ Rottman 2002, p. 228.
^ Glantz 1986; Glantz 1989, pp. 149–159.
^ Kershaw 2001, p. 592.
^ O'Reilly 2001, p. 32.
^ Bellamy 2007, p. 595.
^ O'Reilly 2001, p. 35.
^ Healy 1992, p. 90.
^ Glantz 2001, pp. 50–55.
^ Kolko 1990, p. 45
^ Mazower 2008, p. 362.
^ Hart, Hart & Hughes 2000, p. 151.
^ Blinkhorn 2006, p. 52.
^ Read & Fisher 2002, p. 129.
^ Padfield 1998, pp. 335–336.
^ Kolko 1990, pp. 211, 235, 267–268.
^ Iriye 1981, p. 154.
^ Mitter 2014, p. 286.
^ Polley 2000, p. 148.
^ Beevor 2012, pp. 268–274.
^ Ch'i 1992, p. 161.
^ Hsu & Chang 1971, pp. 412–416, Map 38
^ Weinberg 2005, pp. 660–661.
^ Glantz 2002, pp. 327–366.
^ Glantz 2002, pp. 367–414.
^ Chubarov 2001, p. 122.
^ Holland 2008, pp. 169–184; Beevor 2012, pp. 568–573.
The weeks after the fall of Rome saw a dramatic upswing in German atrocities in Italy (Mazower 2008, pp. 500–502). The period featured massacres with victims in the hundreds at Civitella (de Grazia & Paggi 1991; Belco 2010), Fosse Ardeatine (Portelli 2003), and Sant'Anna di Stazzema (Gordon 2012, pp. 10–11), and is capped with the Marzabotto massacre.
^ Lightbody 2004, p. 224.
^ 
Jump up to:
a b Zeiler 2004, p. 60.
^ Beevor 2012, pp. 555–560.
^ Ch'i 1992, p. 163.
^ Coble 2003, p. 85.
^ Rees 2008, pp. 406–407: "Stalin always believed that Britain and America were delaying the second front so that the Soviet Union would bear the brunt of the war."
^ Weinberg 2005, p. 695.
^ Badsey 1990, p. 91.
^ Dear & Foot 2001, p. 562.
^ Forrest, Evans & Gibbons 2012, p. 191
^ Zaloga 1996, p. 7: "It was the most calamitous defeat of all the German armed forces in World War II."
^ Berend 1996, p. 8.
^ "Slovak National Uprising 1944". Museum of the Slovak National Uprising. Ministry of Foreign and European Affairs of the Slovak Republic. Archived from the original on 19 May 2020. Retrieved 27 April 2020.
^ "Armistice Negotiations and Soviet Occupation". US Library of Congress. Archived from the original on 30 April 2011. Retrieved 14 November 2009. The coup speeded the Red Army's advance, and the Soviet Union later awarded Michael the Order of Victory for his courage in overthrowing Antonescu and putting an end to Romania's war against the Allies. Western historians uniformly point out that the Communists played only a supporting role in the coup; postwar Romanian historians, however, ascribe to the Communists the decisive role in Antonescu's overthrow
^ Evans 2008, p. 653.
^ Wiest & Barbier 2002, pp. 65–66.
^ Wiktor, Christian L (1998). Multilateral Treaty Calendar – 1648–1995. Kluwer Law International. p. 426. ISBN 978-9-0411-0584-4.
^ Shirer 1990, p. 1085.
^ Marston 2005, p. 120.
^ 全面抗战，战犯前仆后继见阎王 [The war criminals tries to be the first to see their ancestors] (in Chinese). Archived from the original on 3 March 2016. Retrieved 16 March 2013.
^ Jowett & Andrew 2002, p. 8.
^ Howard 2004, p. 140.
^ Drea 2003, p. 54.
^ Cook & Bewes 1997, p. 305.
^ Parker 2004, pp. xiii–xiv, 6–8, 68–70, 329–330
^ Glantz 2001, p. 85.
^ Beevor 2012, pp. 709–722.
^ Buchanan 2006, p. 21.
^ Kershaw 2001, pp. 793–829.
^ Shepardson 1998
^ Glass, Andrew (12 April 2016). "President Franklin D. Roosevelt dies at age 63, April 12, 1945". Politico. Retrieved 26 January 2025.
^ O'Reilly 2001, p. 244.
^ Evans 2008, p. 737.
^ Glantz 1998, p. 24.
^ Selby, Scott A. (28 July 2021). The Axmann Conspiracy: The Nazi Plan for a Fourth Reich and How the U.S. Army Defeated It. Scott Andrew Selby. p. 8. Archived from the original on 4 May 2024. Retrieved 4 March 2024.
^ Chant, Christopher (1986). The Encyclopedia of Codenames of World War II. Routledge & Kegan Paul. p. 118. ISBN 978-0-7102-0718-0.
^ Long, Tony (9 March 2011). "March 9, 1945: Burning the Heart Out of the Enemy". Wired. Wired Magazine. Archived from the original on 23 March 2017. Retrieved 22 June 2018. 1945: In the single deadliest air raid of World War II, 330 American B-29s rain incendiary bombs on Tokyo, touching off a firestorm that kills upwards of 100,000 people, burns a quarter of the city to the ground, and leaves a million homeless.
^ Drea 2003, p. 57.
^ Jowett & Andrew 2002, p. 6.
^ Poirier, Michel Thomas (20 October 1999). "Results of the German and American Submarine Campaigns of World War II". U.S. Navy. Archived from the original on 9 April 2008. Retrieved 13 April 2008.
^ Zuberi, Matin (August 2001). "Atomic bombing of Hiroshima and Nagasaki". Strategic Analysis. 25 (5): 623–662. doi:10.1080/09700160108458986. S2CID 154800868.
^ Williams 2006, p. 90.
^ Miscamble 2007, p. 201.
^ Miscamble 2007, pp. 203–204.
^ Ward Wilson. "The Winning Weapon? Rethinking Nuclear Weapons in Light of Hiroshima". International Security, Vol. 31, No. 4 (Spring 2007), pp. 162–179.
^ Glantz 2005.
^ Pape 1993 " The principal cause of Japan's surrender was the ability of the United States to increase the military vulnerability of Japan's home islands, persuading Japanese leaders that defense of the homeland was highly unlikely to succeed. The key military factor causing this effect was the sea blockade, which crippled Japan's ability to produce and equip the forces necessary to execute its strategy. The most important factor accounting for the timing of surrender was the Soviet attack against Manchuria, largely because it persuaded previously adamant Army leaders that the homeland could not be defended.".
^ Bix 2000, pp. 525–526.
^ Bix 2000, pp. 526–528.
^ Beevor 2012, p. 776.
^ Wettig 2008, pp. 96–100.
^ Frei 2002, pp. 41–66.
^ Eberhardt, Piotr (2015). "The Oder-Neisse Line as Poland's western border: As postulated and made a reality". Geographia Polonica. 88 (1): 77–105. doi:10.7163/GPol.0007. Archived from the original on 3 May 2018. Retrieved 3 May 2018.
^ Eberhardt, Piotr (2006). Political Migrations in Poland 1939–1948 (PDF). Warsaw: Didactica. ISBN 978-1-5361-1035-7. Archived from the original (PDF) on 26 June 2015.
^ 
Jump up to:
a b Eberhardt, Piotr (2011). Political Migrations On Polish Territories (1939–1950) (PDF). Warsaw: Polish Academy of Sciences. ISBN 978-8-3615-9046-0. Archived (PDF) from the original on 20 May 2014. Retrieved 3 May 2018.
^ Eberhardt, Piotr (2012). "The Curzon line as the eastern boundary of Poland. The origins and the political background". Geographia Polonica. 85 (1): 5–21. doi:10.7163/GPol.2012.1.1. Archived from the original on 3 May 2018. Retrieved 3 May 2018.
^ Roberts 2006, p. 43.
^ Roberts 2006, p. 55.
^ Shirer 1990, p. 794.
^ Kennedy-Pipe 1995.
^ Wettig 2008, pp. 20–21.
^ Senn 2007, p. ?.
^ "Italy since 1945". Encyclopedia Britannica. Archived from the original on 5 October 2023. Retrieved 2 October 2023.
^ Yoder 1997, p. 39.
^ "History of the UN". United Nations. Archived from the original on 15 December 2021. Retrieved 17 January 2022.
^ "History of the UN". United Nations. Archived from the original on 18 February 2010. Retrieved 25 January 2010.
^ Waltz 2002.
The UDHR is viewable here [1] Archived 3 July 2017 at the Wayback Machine
^ The UN Security Council. Archived from the original on 20 June 2012. Retrieved 15 May 2012.
^ Kantowicz 2000, p. 6.
^ Trachtenberg 1999, p. 33.
^ Applebaum 2012.
^ Naimark 2010.
^ Swain 1992.
^ "Greek Civil War". Encyclopedia Britannica. 28 May 2023. Archived from the original on 24 March 2023. Retrieved 15 May 2023.
^ Borstelmann 2005, p. 318.
^ Leffler & Westad 2010.
^ Weinberg 2005, p. 911.
^ Stueck 2010, p. 71.
^ Lynch 2010, pp. 12–13.
^ Roberts 1997, p. 589.
^ Darwin 2007, pp. 441–443, 464–68.
^ Dear & Foot 2001, p. 1006; Harrison 1998, pp. 34–55.
^ Balabkins 1964, p. 207.
^ Petrov 1967, p. 263.
^ Balabkins 1964, pp. 208–209.
^ "The Bretton Woods Conference, 1944". United States Department of State. 7 January 2008. Archived from the original on 17 April 2022. Retrieved 18 April 2022.
^ DeLong & Eichengreen 1993, pp. 190–191
^ Balabkins 1964, p. 212.
^ Wolf 1993, pp. 29–30, 32
^ Bull & Newell 2005, pp. 20–21
^ Ritchie 1992, p. 23.
^ Minford 1993, p. 117.
^ Schain 2001.
^ Emadi-Coffin 2002, p. 64.
^ Smith 1993, p. 32.
^ Mark Kramer, "The Soviet Bloc and the Cold War in Europe", in Larresm, Klaus, ed. (2014). A Companion to Europe Since 1945. Wiley. p. 79. ISBN 978-1-1188-9024-0.
^ Neary 1992, p. 49.
^ Genzberger, Christine (1994). China Business: The Portable Encyclopedia for Doing Business with China. Petaluma, CA: World Trade Press. p. 4. ISBN 978-0-9631-8643-0.
^ Quick Reference Handbook Set, Basic Knowledge and Modern Technology (revised) by Edward H. Litchfield, Ph.D 1984 p. 195 ISBN 0840740727
^ O'Brien, Joseph V. "World War II: Combatants and Casualties (1937–1945)". Obee's History Page. John Jay College of Criminal Justice. Archived from the original on 25 December 2010. Retrieved 28 December 2013.
^ "World War II Fatalities". secondworldwar.co.uk. Archived from the original on 22 September 2008. Retrieved 20 April 2007.
^ Hosking 2006, p. 242
^ Ellman & Maksudov 1994.
^ Smith 1994, p. 204.
^ Herf 2003.
^ Florida Center for Instructional Technology (2005). "Victims". A Teacher's Guide to the Holocaust. University of South Florida. Archived from the original on 16 May 2016. Retrieved 2 February 2008.
^ 
Jump up to:
a b Niewyk & Nicosia 2000, pp. 45–52.
^ Snyder, Timothy (16 July 2009). "Holocaust: The Ignored Reality". The New York Review of Books. 56 (12). Archived from the original on 10 October 2017. Retrieved 27 August 2017.
^ "Polish Victims". Holocaust Encyclopedia. United States Holocaust Memorial Museum. Archived from the original on 7 May 2016. Retrieved 27 August 2017.
^ "Non-Jewish Holocaust Victims : The 5,000,000 others". BBC. April 2006. Archived from the original on 3 March 2013. Retrieved 4 August 2013.
^ Evans 2008, pp. 158–160, 234–236.
^ Redžić, Enver (2005). Bosnia and Herzegovina in the Second World War. New York: Tylor and Francis. p. 155. ISBN 978-0-7146-5625-0. Archived from the original on 7 March 2023. Retrieved 18 August 2021.
^ Geiger, Vladimir (2012). "Human Losses of the Croats in World War II and the Immediate Post-War Period Caused by the Chetniks (Yugoslav Army in the Fatherand) and the Partisans (People's Liberation Army and the Partisan Detachments of Yugoslavia/Yugoslav Army) and the Communist Authorities: Numerical Indicators". Review of Croatian History. VIII (1). Croatian Institute of History: 117. Archived from the original on 17 November 2015. Retrieved 25 October 2015.
^ Massacre, Volhynia. "The Effects of the Volhynian Massacres". Volhynia Massacre. Archived from the original on 21 June 2018. Retrieved 9 July 2018.
^ "Od rzezi wołyńskiej do akcji Wisła. Konflikt polsko-ukraiński 1943–1947". dzieje.pl (in Polish). Archived from the original on 24 June 2018. Retrieved 10 March 2018.
^ Rummell, R.J. "Statistics". Freedom, Democide, War. The University of Hawaii System. Archived from the original on 23 March 2010. Retrieved 25 January 2010.
^ Dear & Foot 2001, p. 182.
^ Carmichael, Cathie; Maguire, Richard (2015). The Routledge History of Genocide. Routledge. p. 105. ISBN 978-0-3678-6706-5.
^ "A Culture of Cruelty". HistoryNet. 6 November 2017. Archived from the original on 7 May 2022. Retrieved 7 May 2022.
^ Chang 1997, p. 102.
^ Bix 2000, p. ?.
^ Gold, Hal (1996). Unit 731 testimony. Tuttle. pp. 75–77. ISBN 978-0-8048-3565-7.
^ Tucker & Roberts 2004, p. 320.
^ Harris 2002, p. 74.
^ Lee 2002, p. 69.
^ "Japan tested chemical weapons on Aussie POW: new evidence". The Japan Times Online. 27 July 2004. Archived from the original on 29 May 2012. Retrieved 25 January 2010.
^ Kużniar-Plota, Małgorzata (30 November 2004). "Decision to commence investigation into Katyn Massacre". Departmental Commission for the Prosecution of Crimes against the Polish Nation. Retrieved 4 August 2011.
^ Robert Gellately (2007). Lenin, Stalin, and Hitler: The Age of Social Catastrophe. Knopf, ISBN 978-1-4000-4005-6 p. 391
^ Women and War. ABC-CLIO. 2006. pp. 480–. ISBN 978-1-8510-9770-8. Archived from the original on 4 May 2024. Retrieved 14 August 2023.
^ Bird, Nicky (October 2002). "Berlin: The Downfall 1945 by Antony Beevor". International Affairs. 78 (4). Royal Institute of International Affairs: 914–916.
^ Naimark, Norman (1995). The Russians in Germany: A History of the Soviet Zone of Occupation, 1945–1949. Cambridge: Belknap. p. 70.
^ Zur Debatte um die Ausstellung Vernichtungskrieg. Verbrechen der Wehrmacht 1941–1944 im Kieler Landeshaus (Debate on the War of Extermination. Crimes of the Wehrmacht, 1941–1944) Archived 18 July 2011 at the Wayback Machine (PDF). Kiel. 1999.
^ Pascale R . Bos, "Feminists Interpreting the Politics of Wartime Rape: Berlin, 1945"; Yugoslavia, 1992–1993 Journal of Women in Culture and Society, 2006, vol. 31, no. 4, pp. 996–1025
^ Terror from the Sky: The Bombing of German Cities in World War II. Berghahn Books. 2010. p. 167. ISBN 978-1-8454-5844-7.
^ Dower, John (2007). "Lessons from Iwo Jima". Perspectives. 45 (6): 54–56. Archived from the original on 17 January 2011. Retrieved 17 April 2022.
^ The World Must Know: The History of the Holocaust as Told in the United States Holocaust Memorial Museum (2nd ed.), 2006. Washington, DC: United States Holocaust Memorial Museum. ISBN 978-0-8018-8358-3.
^ Herbert 1994, p. 222
^ Overy 2004, pp. 568–569.
^ 
Jump up to:
a b Marek, Michael (27 October 2005). "Final Compensation Pending for Former Nazi Forced Laborers". dw-world.de. Deutsche Welle. Archived from the original on 2 May 2006. Retrieved 19 January 2010.
^ Pearson, Alexander (19 March 2018). "Color photo of girl at Auschwitz strikes chord". Deutsche Welle. Archived from the original on 19 March 2018. Retrieved 12 July 2023. Kwoka was murdered with a phenol injection to the heart a few weeks later.
^ J. Arch Getty, Gábor T. Rittersporn and Viktor N. Zemskov. Victims of the Soviet Penal System in the Pre-War Years: A First Approach on the Basisof Archival Evidence. The American Historical Review, Vol. 98, No. 4 (Oct. 1993), pp. 1017–1049
^ Applebaum 2003, pp. 389–396.
^ Zemskov V. N. On repatriation of Soviet citizens. Istoriya SSSR., 1990, No. 4, (in Russian). See also [2] Archived 14 October 2011 at the Wayback Machine (online version), and Bacon 1992; Ellman 2002.
^ "Japanese Atrocities in the Philippines". American Experience: the Bataan Rescue. PBS Online. Archived from the original on 27 July 2003. Retrieved 18 January 2010.
^ Tanaka 1996, pp. 2–3.
^ Bix 2000, p. 360.
^ 
Jump up to:
a b Ju, Zhifen (June 2002). "Japan's Atrocities of Conscripting and Abusing North China Draftees after the Outbreak of the Pacific War". Joint Study of the Sino-Japanese War: Minutes of the June 2002 Conference. Harvard University Faculty of Arts and Sciences. Archived from the original on 21 May 2012. Retrieved 28 December 2013.
^ 
Jump up to:
a b "Indonesia: World War II and the Struggle For Independence, 1942–50; The Japanese Occupation, 1942–45". Library of Congress. 1992. Archived from the original on 30 October 2004. Retrieved 9 February 2007.
^ Liberman 1996, p. 42.
^ Milward 1992, p. 138.
^ Milward 1992, p. 148.
^ Barber & Harrison 2006, p. 232.
^ Institute of National Remembrance, Polska 1939–1945 Straty osobowe i ofiary represji pod dwiema okupacjami. Materski and Szarota. p. 9 "Total Polish population losses under German occupation are currently calculated at about 2 770 000".
^ Hill 2005, p. 5.
^ Christofferson & Christofferson 2006, p. 156
^ Radtke 1997, p. 107.
^ 
Jump up to:
a b Rahn 2001, p. 266.
^ Leith, C. K. (July 1939). "The Struggle for Mineral Resources". The Annals of the American Academy of Political and Social Science. 204, Democracy and the Americas: 42–48. JSTOR 1021443. Archived from the original on 26 January 2024. Retrieved 26 January 2024. [...] mineral raw materials [...] are the basis of industrial power, and this in turn is the basis of military power. [...] England and the United States of America alone control economic proportions of nearly three-fourths of the world's production of minerals. Not less important, they control the seas over which the products must pass.
^ 
Jump up to:
a b Harrison 1998, p. 3.
^ Compare: Wilson, Mark R. (2016). Destructive Creation: American Business and the Winning of World War II. American Business, Politics, and Society (reprint ed.). Philadelphia: University of Pennsylvania Press. p. 2. ISBN 978-0-8122-9354-8. Archived from the original on 7 March 2023. Retrieved 19 December 2019. By producing nearly two thirds of the munitions used by Allied forces – including huge numbers of aircraft, ships, tanks, trucks, rifles, artillery shells, and bombs – American industry became what President Franklin D. Roosevelt once called 'the arsenal of democracy' [...].
^ Harrison 1998, p. 2.
^ Bernstein 1991, p. 267.
^ Griffith, Charles (1999). The Quest: Haywood Hansell and American Strategic Bombing in World War II. Diane Publishing. p. 203. ISBN 978-1-5856-6069-8.
^ Overy 1994, p. 26.
^ BBSU 1998, p. 84; Lindberg & Todd 2001, p. 126.
^ Unidas, Naciones (2005). World Economic And Social Survey 2004: International Migration. United Nations Pubns. p. 23. ISBN 978-9-2110-9147-2.
^ Tucker & Roberts 2004, p. 76.
^ Levine 1992, p. 227.
^ Klavans, Di Benedetto & Prudom 1997; Ward 2010, pp. 247–251.
^ Tucker & Roberts 2004, p. 163.
^ Bishop, Chris; Chant, Chris (2004). Aircraft Carriers: The World's Greatest Naval Vessels and Their Aircraft. Wigston, Leics: Silverdale Books. p. 7. ISBN 978-1-8450-9079-1.
^ Chenoweth, H. Avery; Nihart, Brooke (2005). Semper Fi: The Definitive Illustrated History of the U.S. Marines. New York: Main Street. p. 180. ISBN 978-1-4027-3099-3.
^ Sumner & Baker 2001, p. 25.
^ Hearn 2007, p. 14.
^ Gardiner & Brown 2004, p. 52.
^ Burcher & Rydill 1995, p. 15.
^ Burcher & Rydill 1995, p. 16.
^ Burns, R. W. (September 1994). "Impact of technology on the defeat of the U-boat September 1939 – May 1943". IEE Proceedings – Science, Measurement and Technology. 141 (5): 343–355. doi:10.1049/ip-smt:19949918 (inactive 1 July 2025).
^ 
Jump up to:
a b Tucker & Roberts 2004, p. 125.
^ Dupuy, Trevor Nevitt (1982). The Evolution of Weapons and Warfare. Jane's Information Group. p. 231. ISBN 978-0-7106-0123-0.
^ "The Vital Role Of Tanks In The Second World War". Imperial War Museums. Archived from the original on 25 March 2022. Retrieved 5 April 2022.
^ Castaldi, Carolina; Fontana, Roberto; Nuvolari, Alessandro (1 August 2009). "'Chariots of fire': the evolution of tank technology, 1915–1945". Journal of Evolutionary Economics. 19 (4): 545–566. doi:10.1007/s00191-009-0141-0. hdl:10419/89322. ISSN 1432-1386. S2CID 36789517.
^ 
Jump up to:
a b Tucker & Roberts 2004, p. 108.
^ Tucker & Roberts 2004, p. 734.
^ 
Jump up to:
a b Cowley & Parker 2001, p. 221.
^ Sprague, Oliver; Griffiths, Hugh (2006). "The AK-47: the worlds favourite killing machine" (PDF). controlarms.org. p. 1. Archived from the original on 28 December 2018. Retrieved 14 November 2009.
^ Ratcliff 2006, p. 11.
^ 
Jump up to:
a b Schoenherr, Steven (2007). "Code Breaking in World War I". History Department at the University of San Diego. Archived from the original on 9 May 2008. Retrieved 15 November 2009.
^ Macintyre, Ben (10 December 2010). "Bravery of thousands of Poles was vital in securing victory". The Times. London. p. 27. Gale IF0504159516.
^ Rowe, Neil C.; Rothstein, Hy. "Deception for Defense of Information Systems: Analogies from Conventional Warfare". Departments of Computer Science and Defense Analysis U.S. Naval Postgraduate School. Air University. Archived from the original on 23 November 2010. Retrieved 15 November 2009.
^ "World War – II". Insights Ias – Simplifying Upsc Ias Exam Preparation. Archived from the original on 11 July 2022. Retrieved 17 September 2022.
^ "Discovery and Development of Penicillin: International Historic Chemical Landmark". Washington, DC: American Chemical Society. Archived from the original on 28 June 2019. Retrieved 15 July 2019.
Sources
Adamthwaite, Anthony P. (1992). The Making of the Second World War. New York: Routledge. ISBN 978-0-415-90716-3.
Anderson, Irvine H. Jr. (1975). "The 1941 De Facto Embargo on Oil to Japan: A Bureaucratic Reflex". The Pacific Historical Review. 44 (2): 201–231. doi:10.2307/3638003. JSTOR 3638003.
Applebaum, Anne (2003). Gulag: A History of the Soviet Camps. London: Allen Lane. ISBN 978-0-7139-9322-6.
——— (2012). Iron Curtain: The Crushing of Eastern Europe 1944–56. London: Allen Lane. ISBN 978-0-7139-9868-9.
Bacon, Edwin (1992). "Glasnost' and the Gulag: New Information on Soviet Forced Labour around World War II". Soviet Studies. 44 (6): 1069–1086. doi:10.1080/09668139208412066. JSTOR 152330.
Badsey, Stephen (1990). Normandy 1944: Allied Landings and Breakout. Oxford: Osprey Publishing. ISBN 978-0-85045-921-0.
Balabkins, Nicholas (1964). Germany Under Direct Controls: Economic Aspects of Industrial Disarmament 1945–1948. New Brunswick, New Jersey: Rutgers University Press.
Barber, John; Harrison, Mark (2006). "Patriotic War, 1941–1945". In Ronald Grigor Suny (ed.). The Cambridge History of Russia – The Twentieth Century. Vol. III. Cambridge: Cambridge University Press. pp. 217–242. ISBN 978-0-521-81144-6.
Barker, A. J. (1971). The Rape of Ethiopia 1936. New York: Ballantine Books. ISBN 978-0-345-02462-6.
Beevor, Antony (1998). Stalingrad. New York: Viking. ISBN 978-0-670-87095-0.
——— (2012). The Second World War. London: Weidenfeld & Nicolson. ISBN 978-0-297-84497-6.
Belco, Victoria (2010). War, Massacre, and Recovery in Central Italy: 1943–1948. Toronto: University of Toronto Press. ISBN 978-0-8020-9314-1.
Bellamy, Chris T. (2007). Absolute War: Soviet Russia in the Second World War. New York: Alfred A. Knopf. ISBN 978-0-375-41086-4.
Ben-Horin, Eliahu (1943). The Middle East: Crossroads of History. New York: W. W. Norton.
Berend, Ivan T. (1996). Central and Eastern Europe, 1944–1993: Detour from the Periphery to the Periphery. Cambridge: Cambridge University Press. ISBN 978-0-521-55066-6.
Bernstein, Gail Lee (1991). Recreating Japanese Women, 1600–1945. Berkeley & Los Angeles: University of California Press. ISBN 978-0-520-07017-2.
Bilhartz, Terry D.; Elliott, Alan C. (2007). Currents in American History: A Brief History of the United States. Armonk, New York: M. E. Sharpe. ISBN 978-0-7656-1821-4.
Bilinsky, Yaroslav (1999). Endgame in NATO's Enlargement: The Baltic States and Ukraine. Westport, Connecticut: Greenwood. ISBN 978-0-275-96363-7.
Bix, Herbert P. (2000). Hirohito and the Making of Modern Japan. New York: HarperCollins. ISBN 978-0-06-019314-0.
Black, Jeremy (2003). World War Two: A Military History. Abingdon & New York: Routledge. ISBN 978-0-415-30534-1.
Blinkhorn, Martin (2006) [1984]. Mussolini and Fascist Italy (3rd ed.). Abingdon & New York: Routledge. ISBN 978-0-415-26206-4.
Bonner, Kit; Bonner, Carolyn (2001). Warship Boneyards. Osceola, Wisconsin: MBI Publishing Company. ISBN 978-0-7603-0870-7.
Borstelmann, Thomas (2005). "The United States, the Cold War, and the colour line". In Melvyn P. Leffler; David S. Painter (eds.). Origins of the Cold War: An International History (2nd ed.). Abingdon & New York: Routledge. pp. 317–332. ISBN 978-0-415-34109-7.
Bosworth, Richard; Maiolo, Joseph (2015). The Cambridge History of the Second World War Volume 2: Politics and Ideology. The Cambridge History of the Second World War (3 vol). Cambridge: Cambridge University Press. pp. 313–314. Archived from the original on 20 August 2016. Retrieved 17 February 2022.
Brayley, Martin J. (2002). The British Army 1939–45, Volume 3: The Far East. Oxford: Osprey Publishing. ISBN 978-1-84176-238-8.
British Bombing Survey Unit (1998). The Strategic Air War Against Germany, 1939–1945. London & Portland, Oregon: Frank Cass Publishers. ISBN 978-0-7146-4722-7.
Brody, J. Kenneth (1999). The Avoidable War: Pierre Laval and the Politics of Reality, 1935–1936. New Brunswick, New Jersey: Transaction Publishers. ISBN 978-0-7658-0622-2.
Brown, David (2004). The Road to Oran: Anglo-French Naval Relations, September 1939 – July 1940. London & New York: Frank Cass. ISBN 978-0-7146-5461-4.
Buchanan, Tom (2006). Europe's Troubled Peace, 1945–2000. Oxford & Malden, Massachusetts: Blackwell Publishing. ISBN 978-0-631-22162-3.
Bueno de Mesquita, Bruce; Smith, Alastair; Siverson, Randolph M.; Morrow, James D. (2003). The Logic of Political Survival. Cambridge, Massachusetts: MIT Press. ISBN 978-0-262-02546-1.
Bull, Martin J.; Newell, James L. (2005). Italian Politics: Adjustment Under Duress. Polity. ISBN 978-0-7456-1298-0.
Bullock, Alan (1990) [1952]. Hitler: A Study in Tyranny. London: Penguin Books. ISBN 978-0-14-013564-0.
Burcher, Roy; Rydill, Louis (1995). "Concepts in Submarine Design". Journal of Applied Mechanics. 62 (1). Cambridge: Cambridge University Press: 268. Bibcode:1995JAM....62R.268B. doi:10.1115/1.2895927. ISBN 978-0-521-55926-3.
Busky, Donald F. (2002). Communism in History and Theory: Asia, Africa, and the Americas. Westport, Connecticut: Praeger Publishers. ISBN 978-0-275-97733-7.
Canfora, Luciano (2006) [2004]. Democracy in Europe: A History. Oxford & Malden MA: Blackwell Publishing. ISBN 978-1-4051-1131-7.
Cantril, Hadley (1940). "America Faces the War: A Study in Public Opinion". Public Opinion Quarterly. 4 (3): 387–407. doi:10.1086/265420. JSTOR 2745078.
Chang, Iris (1997). The Rape of Nanking: The Forgotten Holocaust of World War II. New York: Basic Books. ISBN 978-0-465-06835-7.
Christofferson, Thomas R.; Christofferson, Michael S. (2006). France During World War II: From Defeat to Liberation. New York: Fordham University Press. ISBN 978-0-8232-2562-0.
Chubarov, Alexander (2001). Russia's Bitter Path to Modernity: A History of the Soviet and Post-Soviet Eras. London & New York: Continuum. ISBN 978-0-8264-1350-5.
Ch'i, Hsi-Sheng (1992). "The Military Dimension, 1942–1945". In James C. Hsiung; Steven I. Levine (eds.). China's Bitter Victory: War with Japan, 1937–45. Armonk, New York: M. E. Sharpe. pp. 157–184. ISBN 978-1-56324-246-5.
Cienciala, Anna M. (2010). "Another look at the Poles and Poland during World War II". The Polish Review. 55 (1): 123–143. doi:10.2307/25779864. JSTOR 25779864. S2CID 159445902.
Clogg, Richard (2002). A Concise History of Greece (2nd ed.). Cambridge: Cambridge University Press. ISBN 978-0-521-80872-9.
Coble, Parks M. (2003). Chinese Capitalists in Japan's New Order: The Occupied Lower Yangzi, 1937–1945. Berkeley & Los Angeles: University of California Press. ISBN 978-0-520-23268-6.
Collier, Paul (2003). The Second World War (4): The Mediterranean 1940–1945. Oxford: Osprey Publishing. ISBN 978-1-84176-539-6.
Collier, Martin; Pedley, Philip (2000). Germany 1919–45. Oxford: Heinemann. ISBN 978-0-435-32721-7.
Commager, Henry Steele (2004). The Story of the Second World War. Brassey's. ISBN 978-1-57488-741-9.
Coogan, Anthony (1993). "The Volunteer Armies of Northeast China". History Today. 43. Archived from the original on 11 May 2012. Retrieved 6 May 2012.
Cook, Chris; Bewes, Diccon (1997). What Happened Where: A Guide to Places and Events in Twentieth-Century History. London: UCL Press. ISBN 978-1-85728-532-1.
Cowley, Robert; Parker, Geoffrey, eds. (2001). The Reader's Companion to Military History. Boston: Houghton Mifflin Company. ISBN 978-0-618-12742-9.
Darwin, John (2007). After Tamerlane: The Rise & Fall of Global Empires 1400–2000. London: Penguin Books. ISBN 978-0-14-101022-9.
Davies, Norman (2006). Europe at War 1939–1945: No Simple Victory. London: Macmillan. ix+544 pages. ISBN 978-0-333-69285-1. OCLC 70401618.
Dear, I. C. B.; Foot, M. R. D., eds. (2001) [1995]. The Oxford Companion to World War II. Oxford: Oxford University Press. ISBN 978-0-19-860446-4.
DeLong, J. Bradford; Eichengreen, Barry (1993). "The Marshall Plan: History's Most Successful Structural Adjustment Program". In Rudiger Dornbusch; Wilhelm Nölling; Richard Layard (eds.). Postwar Economic Reconstruction and Lessons for the East Today. Cambridge, Massachusetts: MIT Press. pp. 189–230. ISBN 978-0-262-04136-2.
Dower, John W. (1986). War Without Mercy: Race and Power in the Pacific War. New York: Pantheon Books. ISBN 978-0-394-50030-0.
Drea, Edward J. (2003). In the Service of the Emperor: Essays on the Imperial Japanese Army. Lincoln, Nebraska: University of Nebraska Press. ISBN 978-0-8032-6638-4.
de Grazia, Victoria; Paggi, Leonardo (Autumn 1991). "Story of an Ordinary Massacre: Civitella della Chiana, 29 June, 1944". Cardozo Studies in Law and Literature. 3 (2): 153–169. doi:10.1525/lal.1991.3.2.02a00030. JSTOR 743479.
Dunn, Dennis J. (1998). Caught Between Roosevelt & Stalin: America's Ambassadors to Moscow. Lexington, Kentucky: University Press of Kentucky. ISBN 978-0-8131-2023-2.
Eastman, Lloyd E. (1986). "Nationalist China during the Sino-Japanese War 1937–1945". In John K. Fairbank; Denis Twitchett (eds.). The Cambridge History of China – Republican China 1912–1949, Part 2. Vol. 13. Cambridge: Cambridge University Press. ISBN 978-0-521-24338-4.
Ellman, Michael (2002). "Soviet Repression Statistics: Some Comments" (PDF). Europe-Asia Studies. 54 (7): 1151–1172. doi:10.1080/0966813022000017177. JSTOR 826310. S2CID 43510161. Archived from the original (PDF) on 22 November 2012. Copy
———; Maksudov, S. (1994). "Soviet Deaths in the Great Patriotic War: A Note" (PDF). Europe-Asia Studies. 46 (4): 671–680. doi:10.1080/09668139408412190. JSTOR 152934. PMID 12288331. Archived (PDF) from the original on 13 February 2022. Retrieved 17 February 2022.
Emadi-Coffin, Barbara (2002). Rethinking International Organization: Deregulation and Global Governance. London & New York: Routledge. ISBN 978-0-415-19540-9.
Erickson, John (2001). "Moskalenko". In Shukman, Harold (ed.). Stalin's Generals. London: Phoenix Press. pp. 137–154. ISBN 978-1-84212-513-7.
——— (2003). The Road to Stalingrad. London: Cassell Military. ISBN 978-0-304-36541-8.
Evans, David C.; Peattie, Mark R. (2012) [1997]. Kaigun: Strategy, Tactics, and Technology in the Imperial Japanese Navy. Annapolis, Maryland: Naval Institute Press. ISBN 978-1-59114-244-7.
Evans, Richard J. (2008). The Third Reich at War. London: Allen Lane. ISBN 978-0-7139-9742-2.
Fairbank, John King; Goldman, Merle (2006) [1994]. China: A New History (2nd ed.). Cambridge: Harvard University Press. ISBN 978-0-674-01828-0.
Farrell, Brian P. (1993). "Yes, Prime Minister: Barbarossa, Whipcord, and the Basis of British Grand Strategy, Autumn 1941". Journal of Military History. 57 (4): 599–625. doi:10.2307/2944096. JSTOR 2944096.
Ferguson, Niall (2006). The War of the World: Twentieth-Century Conflict and the Descent of the West. Penguin. ISBN 978-0-14-311239-6.
Forrest, Glen; Evans, Anthony; Gibbons, David (2012). The Illustrated Timeline of Military History. New York: Rosen. ISBN 978-1-4488-4794-5.
Förster, Jürgen (1998). "Hitler's Decision in Favour of War". In Horst Boog; Jürgen Förster; Joachim Hoffmann; Ernst Klink; Rolf-Dieter Muller; Gerd R. Ueberschar (eds.). Germany and the Second World War – The Attack on the Soviet Union. Vol. IV. Oxford: Clarendon Press. pp. 13–52. ISBN 978-0-19-822886-8.
Förster, Stig; Gessler, Myriam (2005). "The Ultimate Horror: Reflections on Total War and Genocide". In Roger Chickering; Stig Förster; Bernd Greiner (eds.). A World at Total War: Global Conflict and the Politics of Destruction, 1937–1945. Cambridge: Cambridge University Press. pp. 53–68. ISBN 978-0-521-83432-2.
Frank, Richard B. (2020). Tower of Skulls: A History of The Asia-Pacific War July 1937-May 1942. W. W. Norton & Company. p. 161. ISBN 978-1-324-00210-9.
Frei, Norbert (2002). Adenauer's Germany and the Nazi Past: The Politics of Amnesty and Integration. New York: Columbia University Press. ISBN 978-0-231-11882-8.
Gardiner, Robert; Brown, David K., eds. (2004). The Eclipse of the Big Gun: The Warship 1906–1945. London: Conway Maritime Press. ISBN 978-0-85177-953-9.
Garver, John W. (1988). Chinese-Soviet Relations, 1937–1945: The Diplomacy of Chinese Nationalism. New York: Oxford University Press. ISBN 978-0-19-505432-3.
Gilbert, Martin (1989). Second World War. London: Weidenfeld and Nicolson. ISBN 978-0-297-79616-9.
Glantz, David M. (1986). "Soviet Defensive Tactics at Kursk, July 1943". Combined Arms Research Library. CSI Report No. 11. Command and General Staff College. OCLC 278029256. Archived from the original on 6 March 2008. Retrieved 15 July 2013.
——— (1989). Soviet Military Deception in the Second World War. Abingdon & New York: Frank Cass. ISBN 978-0-7146-3347-3.
——— (1998). When Titans Clashed: How the Red Army Stopped Hitler. Lawrence, Kansas: University Press of Kansas. ISBN 978-0-7006-0899-7.
——— (2001). "The Soviet-German War 1941–45 Myths and Realities: A Survey Essay" (PDF). Archived from the original (PDF) on 9 July 2011.
——— (2002). The Battle for Leningrad: 1941–1944. Lawrence, Kansas: University Press of Kansas. ISBN 978-0-7006-1208-6.
——— (2005). "August Storm: The Soviet Strategic Offensive in Manchuria". Combined Arms Research Library. Leavenworth Papers. Command and General Staff College. OCLC 78918907. Archived from the original on 2 March 2008. Retrieved 15 July 2013.
Goldstein, Margaret J. (2004). World War II: Europe. Minneapolis: Lerner Publications. ISBN 978-0-8225-0139-8.
Gordon, Andrew (2004). "The greatest military armada ever launched". In Jane Penrose (ed.). The D-Day Companion. Oxford: Osprey Publishing. pp. 127–144. ISBN 978-1-84176-779-6.
Gordon, Robert S. C. (2012). The Holocaust in Italian Culture, 1944–2010. Stanford, California: Stanford University Press. ISBN 978-0-8047-6346-2.
Grove, Eric J. (1995). "A Service Vindicated, 1939–1946". In J. R. Hill (ed.). The Oxford Illustrated History of the Royal Navy. Oxford: Oxford University Press. pp. 348–380. ISBN 978-0-19-211675-8.
Hane, Mikiso (2001). Modern Japan: A Historical Survey (3rd ed.). Boulder, Colorado: Westview Press. ISBN 978-0-8133-3756-2.
Hanhimäki, Jussi M. (1997). Containing Coexistence: America, Russia, and the "Finnish Solution". Kent, Ohio: Kent State University Press. ISBN 978-0-87338-558-9.
Harris, Sheldon H. (2002). Factories of Death: Japanese Biological Warfare, 1932–1945, and the American Cover-up (2nd ed.). London & New York: Routledge. ISBN 978-0-415-93214-1.
Harrison, Mark (1998). "The economics of World War II: an overview". In Mark Harrison (ed.). The Economics of World War II: Six Great Powers in International Comparison. Cambridge: Cambridge University Press. pp. 1–42. ISBN 978-0-521-62046-8.
Hart, Stephen; Hart, Russell; Hughes, Matthew (2000). The German Soldier in World War II. Osceola, Wisconsin: MBI Publishing Company. ISBN 978-1-86227-073-2.
Hauner, Milan (1978). "Did Hitler Want a World Dominion?". Journal of Contemporary History. 13 (1): 15–32. doi:10.1177/002200947801300102. JSTOR 260090. S2CID 154865385.
Healy, Mark (1992). Kursk 1943: The Tide Turns in the East. Oxford: Osprey Publishing. ISBN 978-1-85532-211-0.
Hearn, Chester G. (2007). Carriers in Combat: The Air War at Sea. Mechanicsburg, Pennsylvania: Stackpole Books. ISBN 978-0-8117-3398-4.
Hempel, Andrew (2005). Poland in World War II: An Illustrated Military History. New York: Hippocrene Books. ISBN 978-0-7818-1004-3.
Herbert, Ulrich (1994). "Labor as spoils of conquest, 1933–1945". In David F. Crew (ed.). Nazism and German Society, 1933–1945. London & New York: Routledge. pp. 219–273. ISBN 978-0-415-08239-6.
Herf, Jeffrey (2003). "The Nazi Extermination Camps and the Ally to the East. Could the Red Army and Air Force Have Stopped or Slowed the Final Solution?". Kritika: Explorations in Russian and Eurasian History. 4 (4): 913–930. doi:10.1353/kri.2003.0059. S2CID 159958616.
Hill, Alexander (2005). The War Behind The Eastern Front: The Soviet Partisan Movement In North-West Russia 1941–1944. London & New York: Frank Cass. ISBN 978-0-7146-5711-0.
Holland, James (2008). Italy's Sorrow: A Year of War 1944–45. London: HarperPress. ISBN 978-0-00-717645-8.
Hosking, Geoffrey A. (2006). Rulers and Victims: The Russians in the Soviet Union. Cambridge: Harvard University Press. ISBN 978-0-674-02178-5.
Howard, Joshua H. (2004). Workers at War: Labor in China's Arsenals, 1937–1953. Stanford, California: Stanford University Press. ISBN 978-0-8047-4896-4.
Hsu, Long-hsuen; Chang, Ming-kai (1971). History of The Sino-Japanese War (1937–1945) (2nd ed.). Chung Wu Publishers. ASIN B00005W210. OCLC 12828898.
Ingram, Norman (2006). "Pacifism". In Lawrence D. Kritzman; Brian J. Reilly (eds.). The Columbia History Of Twentieth-Century French Thought. New York: Columbia University Press. pp. 76–78. ISBN 978-0-231-10791-4.
Iriye, Akira (1981). Power and Culture: The Japanese-American War, 1941–1945. Cambridge, Massachusetts: Harvard University Press. ISBN 978-0-674-69580-1.
Jackson, Ashley (2006). The British Empire and the Second World War. London & New York: Hambledon Continuum. ISBN 978-1-85285-417-1.
Joes, Anthony James (2004). Resisting Rebellion: The History And Politics of Counterinsurgency. Lexington: University Press of Kentucky. ISBN 978-0-8131-2339-4.
Jowett, Philip S. (2001). The Italian Army 1940–45, Volume 2: Africa 1940–43. Oxford: Osprey Publishing. ISBN 978-1-85532-865-5.
———; Andrew, Stephen (2002). The Japanese Army, 1931–45. Oxford: Osprey Publishing. ISBN 978-1-84176-353-8.
Jukes, Geoffrey (2001). "Kuznetzov". In Harold Shukman (ed.). Stalin's Generals. London: Phoenix Press. pp. 109–116. ISBN 978-1-84212-513-7.
Kantowicz, Edward R. (1999). The Rage of Nations. Grand Rapids, Michigan: William B. Eerdmans. ISBN 978-0-8028-4455-2.
——— (2000). Coming Apart, Coming Together. Grand Rapids, Michigan: William B. Eerdmans. ISBN 978-0-8028-4456-9.
Keeble, Curtis (1990). "The historical perspective". In Alex Pravda; Peter J. Duncan (eds.). Soviet-British Relations Since the 1970s. Cambridge: Cambridge University Press. ISBN 978-0-521-37494-1.
Keegan, John (1997). The Second World War. London: Pimlico. ISBN 978-0-7126-7348-8.
Kennedy, David M. (2001). Freedom from Fear: The American People in Depression and War, 1929–1945. Oxford University Press. ISBN 978-0-19-514403-1.
Kennedy-Pipe, Caroline (1995). Stalin's Cold War: Soviet Strategies in Europe, 1943–56. Manchester: Manchester University Press. ISBN 978-0-7190-4201-0.
Kershaw, Ian (2001). Hitler, 1936–1945: Nemesis. New York: W. W. Norton. ISBN 978-0-393-04994-7.
——— (2007). Fateful Choices: Ten Decisions That Changed the World, 1940–1941. London: Allen Lane. ISBN 978-0-7139-9712-5.
Kitson, Alison (2001). Germany 1858–1990: Hope, Terror, and Revival. Oxford: Oxford University Press. ISBN 978-0-19-913417-5.
Klavans, Richard A.; Di Benedetto, C. Anthony; Prudom, Melanie J. (1997). "Understanding Competitive Interactions: The U.S. Commercial Aircraft Market". Journal of Managerial Issues. 9 (1): 13–361. JSTOR 40604127.
Kleinfeld, Gerald R. (1983). "Hitler's Strike for Tikhvin". Military Affairs. 47 (3): 122–128. doi:10.2307/1988082. JSTOR 1988082.
Koch, H. W. (1983). "Hitler's 'Programme' and the Genesis of Operation 'Barbarossa'". The Historical Journal. 26 (4): 891–920. doi:10.1017/S0018246X00012747. JSTOR 2639289. S2CID 159671713.
Kolko, Gabriel (1990) [1968]. The Politics of War: The World and United States Foreign Policy, 1943–1945. New York: Random House. ISBN 978-0-679-72757-6.
Laurier, Jim (2001). Tobruk 1941: Rommel's Opening Move. Oxford: Osprey Publishing. ISBN 978-1-84176-092-6.
Lee, En-han (2002). "The Nanking Massacre Reassessed: A Study of the Sino-Japanese Controversy over the Factual Number of Massacred Victims". In Robert Sabella; Fei Fei Li; David Liu (eds.). Nanking 1937: Memory and Healing. Armonk, New York: M. E. Sharpe. pp. 47–74. ISBN 978-0-7656-0816-1.
Leffler, Melvyn P.; Westad, Odd Arne, eds. (2010). The Cambridge History of the Cold War. Cambridge: Cambridge University Press. ISBN 978-0-521-83938-9, in 3 volumes.
Levine, Alan J. (1992). The Strategic Bombing of Germany, 1940–1945. Westport, Connecticut: Praeger. ISBN 978-0-275-94319-6.
Lewis, Morton (1953). "Japanese Plans and American Defenses". In Greenfield, Kent Roberts (ed.). The Fall of the Philippines. Washington, D.C.: US Government Printing Office. LCCN 53-63678. Archived from the original on 8 January 2012. Retrieved 1 October 2009.
Liberman, Peter (1996). Does Conquest Pay?: The Exploitation of Occupied Industrial Societies. Princeton, New Jersey: Princeton University Press. ISBN 978-0-691-02986-3.
Liddell Hart, Basil (1977). History of the Second World War (4th ed.). London: Pan. ISBN 978-0-330-23770-3.
Lightbody, Bradley (2004). The Second World War: Ambitions to Nemesis. London & New York: Routledge. ISBN 978-0-415-22404-8.
Lindberg, Michael; Todd, Daniel (2001). Brown-, Green- and Blue-Water Fleets: the Influence of Geography on Naval Warfare, 1861 to the Present. Westport, Connecticut: Praeger. ISBN 978-0-275-96486-3.
Lowe, C. J.; Marzari, F. (2002). Italian Foreign Policy 1870–1940. London: Routledge. ISBN 978-0-415-26681-9.
Lynch, Michael (2010). The Chinese Civil War 1945–49. Oxford: Osprey Publishing. ISBN 978-1-84176-671-3.
Maddox, Robert James (1992). The United States and World War II. Boulder, Colorado: Westview Press. ISBN 978-0-8133-0437-3.
Maingot, Anthony P. (1994). The United States and the Caribbean: Challenges of an Asymmetrical Relationship. Boulder, Colorado: Westview Press. ISBN 978-0-8133-2241-4.
Mandelbaum, Michael (1988). The Fate of Nations: The Search for National Security in the Nineteenth and Twentieth Centuries. Cambridge University Press. p. 96. ISBN 978-0-521-35790-6.
Marston, Daniel (2005). The Pacific War Companion: From Pearl Harbor to Hiroshima. Oxford: Osprey Publishing. ISBN 978-1-84176-882-3.
Masaya, Shiraishi (1990). Japanese Relations with Vietnam, 1951–1987. Ithaca, New York: SEAP Publications. ISBN 978-0-87727-122-2.
May, Ernest R. (1955). "The United States, the Soviet Union, and the Far Eastern War, 1941–1945". Pacific Historical Review. 24 (2): 153–174. doi:10.2307/3634575. JSTOR 3634575.
Mazower, Mark (2008). Hitler's Empire: Nazi Rule in Occupied Europe. London: Allen Lane. ISBN 978-1-59420-188-2.
Milner, Marc (1990). "The Battle of the Atlantic". In Gooch, John (ed.). Decisive Campaigns of the Second World War. Abingdon: Frank Cass. pp. 45–66. ISBN 978-0-7146-3369-5.
Milward, A. S. (1964). "The End of the Blitzkrieg". The Economic History Review. 16 (3): 499–518. JSTOR 2592851.
——— (1992) [1977]. War, Economy, and Society, 1939–1945. Berkeley, California: University of California Press. ISBN 978-0-520-03942-1.
Minford, Patrick (1993). "Reconstruction and the UK Postwar Welfare State: False Start and New Beginning". In Rudiger Dornbusch; Wilhelm Nölling; Richard Layard (eds.). Postwar Economic Reconstruction and Lessons for the East Today. Cambridge, Massachusetts: MIT Press. pp. 115–138. ISBN 978-0-262-04136-2.
Mingst, Karen A.; Karns, Margaret P. (2007). United Nations in the Twenty-First Century (3rd ed.). Boulder, Colorado: Westview Press. ISBN 978-0-8133-4346-4.
Miscamble, Wilson D. (2007). From Roosevelt to Truman: Potsdam, Hiroshima, and the Cold War. New York: Cambridge University Press. ISBN 978-0-521-86244-8.
Mitcham, Samuel W. (2007) [1982]. Rommel's Desert War: The Life and Death of the Afrika Korps. Mechanicsburg, Pennsylvania: Stackpole Books. ISBN 978-0-8117-3413-4.
Mitter, Rana (2014). Forgotten Ally: China's World War II, 1937–1945. Mariner Books. ISBN 978-0-544-33450-2.
Molinari, Andrea (2007). Desert Raiders: Axis and Allied Special Forces 1940–43. Oxford: Osprey Publishing. ISBN 978-1-84603-006-2.
Murray, Williamson (1983). Strategy for Defeat: The Luftwaffe, 1933–1945. Maxwell Air Force Base, Alabama: Air University Press. ISBN 978-1-4294-9235-5. Archived from the original on 24 January 2022. Retrieved 17 February 2022.
———; Millett, Allan Reed (2001). A War to Be Won: Fighting the Second World War. Cambridge, Massachusetts: Harvard University Press. ISBN 978-0-674-00680-5.
Myers, Ramon; Peattie, Mark (1987). The Japanese Colonial Empire, 1895–1945. Princeton, New Jersey: Princeton University Press. ISBN 978-0-691-10222-1.
Naimark, Norman (2010). "The Sovietization of Eastern Europe, 1944–1953". In Melvyn P. Leffler; Odd Arne Westad (eds.). The Cambridge History of the Cold War – Origins. Vol. I. Cambridge: Cambridge University Press. pp. 175–197. ISBN 978-0-521-83719-4.
Neary, Ian (1992). "Japan". In Martin Harrop (ed.). Power and Policy in Liberal Democracies. Cambridge: Cambridge University Press. pp. 49–70. ISBN 978-0-521-34579-8.
Neillands, Robin (2005). The Dieppe Raid: The Story of the Disastrous 1942 Expedition. Bloomington, Indiana: Indiana University Press. ISBN 978-0-253-34781-7.
Neulen, Hans Werner (2000). In the skies of Europe – Air Forces allied to the Luftwaffe 1939–1945. Ramsbury, Marlborough, United Kingdom: The Crowood Press. ISBN 978-1-86126-799-3.
Niewyk, Donald L.; Nicosia, Francis (2000). The Columbia Guide to the Holocaust. New York: Columbia University Press. ISBN 978-0-231-11200-0.
Overy, Richard (1994). War and Economy in the Third Reich. New York: Clarendon Press. ISBN 978-0-19-820290-5.
——— (1995). Why the Allies Won. London: Pimlico. ISBN 978-0-7126-7453-9.
——— (2004). The Dictators: Hitler's Germany, Stalin's Russia. New York: W. W. Norton. ISBN 978-0-393-02030-4.
———; Wheatcroft, Andrew (1999). The Road to War (2nd ed.). London: Penguin Books. ISBN 978-0-14-028530-7.
O'Reilly, Charles T. (2001). Forgotten Battles: Italy's War of Liberation, 1943–1945. Lanham, Maryland: Lexington Books. ISBN 978-0-7391-0195-7.
Painter, David S. (2012). "Oil and the American Century". The Journal of American History. 99 (1): 24–39. doi:10.1093/jahist/jas073.
Padfield, Peter (1998). War Beneath the Sea: Submarine Conflict During World War II. New York: John Wiley. ISBN 978-0-471-24945-0.
Pape, Robert A. (1993). "Why Japan Surrendered". International Security. 18 (2): 154–201. doi:10.2307/2539100. JSTOR 2539100. S2CID 153741180.
Parker, Danny S. (2004). Battle of the Bulge: Hitler's Ardennes Offensive, 1944–1945 (New ed.). Cambridge, Massachusetts: Da Capo Press. ISBN 978-0-306-81391-7.
Payne, Stanley G. (2008). Franco and Hitler: Spain, Germany, and World War II. New Haven, Connecticut: Yale University Press. ISBN 978-0-300-12282-4.
Perez, Louis G. (1998). The History of Japan. Westport, Connecticut: Greenwood Publishing Group. ISBN 978-0-313-30296-1.
Petrov, Vladimir (1967). Money and Conquest: Allied Occupation Currencies in World War II. Baltimore, Maryland: Johns Hopkins University Press. ISBN 978-0-8018-0530-1.
Polley, Martin (2000). An A–Z of Modern Europe Since 1789. London & New York: Routledge. ISBN 978-0-415-18597-4.
Portelli, Alessandro (2003). The Order Has Been Carried Out: History, Memory, and Meaning of a Nazi Massacre in Rome. Basingstoke & New York: Palgrave Macmillan. ISBN 978-1-4039-8008-3.
Preston, P. W. (1998). Pacific Asia in the Global System: An Introduction. Oxford & Malden, Massachusetts: Blackwell Publishers. ISBN 978-0-631-20238-7.
Prins, Gwyn (2002). The Heart of War: On Power, Conflict and Obligation in the Twenty-First Century. London & New York: Routledge. ISBN 978-0-415-36960-2.
Radtke, K. W. (1997). "'Strategic' concepts underlying the so-called Hirota foreign policy, 1933–7". In Aiko Ikeo (ed.). Economic Development in Twentieth Century East Asia: The International Context. London & New York: Routledge. pp. 100–120. ISBN 978-0-415-14900-6.
Rahn, Werner (2001). "The War in the Pacific". In Horst Boog; Werner Rahn; Reinhard Stumpf; Bernd Wegner (eds.). Germany and the Second World War – The Global War. Vol. VI. Oxford: Clarendon Press. pp. 191–298. ISBN 978-0-19-822888-2.
Ratcliff, R. A. (2006). Delusions of Intelligence: Enigma, Ultra, and the End of Secure Ciphers. New York: Cambridge University Press. ISBN 978-0-521-85522-8.
Read, Anthony (2004). The Devil's Disciples: Hitler's Inner Circle. New York: W. W. Norton. ISBN 978-0-393-04800-1.
Read, Anthony; Fisher, David (2002) [1992]. The Fall Of Berlin. London: Pimlico. ISBN 978-0-7126-0695-0.
Record, Jeffery (2005). Appeasement Reconsidered: Investigating the Mythology of the 1930s (PDF). Diane Publishing. p. 50. ISBN 978-1-58487-216-0. Archived from the original (PDF) on 11 April 2010. Retrieved 15 November 2009.
Rees, Laurence (2008). World War II Behind Closed Doors: Stalin, the Nazis and the West. London: BBC Books. ISBN 978-0-563-49335-8.
Regan, Geoffrey (2004). The Brassey's Book of Military Blunders. Brassey's. ISBN 978-1-57488-252-0.
Reinhardt, Klaus (1992). Moscow – The Turning Point: The Failure of Hitler's Strategy in the Winter of 1941–42. Oxford: Berg. ISBN 978-0-85496-695-0.
Reynolds, David (2006). From World War to Cold War: Churchill, Roosevelt, and the International History of the 1940s. Oxford University Press. ISBN 978-0-19-928411-5.
Rich, Norman (1992) [1973]. Hitler's War Aims, Volume I: Ideology, the Nazi State, and the Course of Expansion. New York: W. W. Norton. ISBN 978-0-393-00802-9.
Ritchie, Ella (1992). "France". In Martin Harrop (ed.). Power and Policy in Liberal Democracies. Cambridge: Cambridge University Press. pp. 23–48. ISBN 978-0-521-34579-8.
Roberts, Cynthia A. (1995). "Planning for War: The Red Army and the Catastrophe of 1941". Europe-Asia Studies. 47 (8): 1293–1326. doi:10.1080/09668139508412322. JSTOR 153299.
Roberts, Geoffrey (2006). Stalin's Wars: From World War to Cold War, 1939–1953. New Haven, Connecticut: Yale University Press. ISBN 978-0-300-11204-7.
Roberts, J. M. (1997). The Penguin History of Europe. London: Penguin Books. ISBN 978-0-14-026561-3.
Ropp, Theodore (2000). War in the Modern World (Revised ed.). Baltimore, Maryland: Johns Hopkins University Press. ISBN 978-0-8018-6445-2.
Roskill, S. W. (1954). The War at Sea 1939–1945, Volume 1: The Defensive. History of the Second World War. United Kingdom Military Series. London: HMSO. Archived from the original on 4 January 2022. Retrieved 17 February 2022.
Ross, Steven T. (1997). American War Plans, 1941–1945: The Test of Battle. Abingdon & New York: Routledge. ISBN 978-0-7146-4634-3.
Rottman, Gordon L. (2002). World War II Pacific Island Guide: A Geo-Military Study. Westport, Connecticut: Greenwood Press. ISBN 978-0-313-31395-0.
Rotundo, Louis (1986). "The Creation of Soviet Reserves and the 1941 Campaign". Military Affairs. 50 (1): 21–28. doi:10.2307/1988530. JSTOR 1988530.
Salecker, Gene Eric (2001). Fortress Against the Sun: The B-17 Flying Fortress in the Pacific. Conshohocken, Pennsylvania: Combined Publishing. ISBN 978-1-58097-049-5.
Schain, Martin A., ed. (2001). The Marshall Plan Fifty Years Later. London: Palgrave Macmillan. ISBN 978-0-333-92983-4.
Schmitz, David F. (2000). Henry L. Stimson: The First Wise Man. Lanham, Maryland: Rowman & Littlefield. ISBN 978-0-8420-2632-1.
Schoppa, R. Keith (2011). In a Sea of Bitterness, Refugees during the Sino-Japanese War. Harvard University Press. ISBN 978-0-674-05988-7.
Sella, Amnon (1978). ""Barbarossa": Surprise Attack and Communication". Journal of Contemporary History. 13 (3): 555–583. doi:10.1177/002200947801300308. JSTOR 260209. S2CID 220880174.
——— (1983). "Khalkhin-Gol: The Forgotten War". Journal of Contemporary History. 18 (4): 651–687. JSTOR 260307.
Senn, Alfred Erich (2007). Lithuania 1940: Revolution from Above. Amsterdam & New York: Rodopi. ISBN 978-9-0420-2225-6.
Shaw, Anthony (2000). World War II: Day by Day. Osceola, Wisconsin: MBI Publishing Company. ISBN 978-0-7603-0939-1.
Shepardson, Donald E. (1998). "The Fall of Berlin and the Rise of a Myth". Journal of Military History. 62 (1): 135–154. doi:10.2307/120398. JSTOR 120398.
Shirer, William L. (1990) [1960]. The Rise and Fall of the Third Reich: A History of Nazi Germany. New York: Simon & Schuster. ISBN 978-0-671-72868-7.
Shore, Zachary (2003). What Hitler Knew: The Battle for Information in Nazi Foreign Policy. New York: Oxford University Press. ISBN 978-0-19-518261-3.
Slim, William (1956). Defeat into Victory. London: Cassell.
Smith, Alan (1993). Russia and the World Economy: Problems of Integration. London: Routledge. ISBN 978-0-415-08924-1.
Smith, J. W. (1994). The World's Wasted Wealth 2: Save Our Wealth, Save Our Environment. Institute for Economic Democracy. ISBN 978-0-9624423-2-2.
Smith, Peter C. (2002) [1970]. Pedestal: The Convoy That Saved Malta (5th ed.). Manchester: Goodall. ISBN 978-0-907579-19-9.
Smith, David J.; Pabriks, Artis; Purs, Aldis; Lane, Thomas (2002). The Baltic States: Estonia, Latvia and Lithuania. London: Routledge. ISBN 978-0-415-28580-3.
Smith, Winston; Steadman, Ralph (2004). All Riot on the Western Front, Volume 3. Last Gasp. ISBN 978-0-86719-616-0.
Snyder, Timothy (2010). Bloodlands: Europe Between Hitler and Stalin. London: The Bodley Head. ISBN 978-0-224-08141-2.
Spring, D. W. (1986). "The Soviet Decision for War against Finland, 30 November 1939". Soviet Studies. 38 (2): 207–226. doi:10.1080/09668138608411636. JSTOR 151203. S2CID 154270850.
Steinberg, Jonathan (1995). "The Third Reich Reflected: German Civil Administration in the Occupied Soviet Union, 1941–4". The English Historical Review. 110 (437): 620–651. doi:10.1093/ehr/cx.437.620. JSTOR 578338.
Steury, Donald P. (1987). "Naval Intelligence, the Atlantic Campaign and the Sinking of the Bismarck: A Study in the Integration of Intelligence into the Conduct of Naval Warfare". Journal of Contemporary History. 22 (2): 209–233. doi:10.1177/002200948702200202. JSTOR 260931. S2CID 159943895.
Stueck, William (2010). "The Korean War". In Melvyn P. Leffler; Odd Arne Westad (eds.). The Cambridge History of the Cold War – Origins. Vol. I. Cambridge: Cambridge University Press. pp. 266–287. ISBN 978-0-521-83719-4.
Sumner, Ian; Baker, Alix (2001). The Royal Navy 1939–45. Oxford: Osprey Publishing. ISBN 978-1-84176-195-4.
Swain, Bruce (2001). A Chronology of Australian Armed Forces at War 1939–45. Crows Nest: Allen & Unwin. ISBN 978-1-86508-352-0.
Swain, Geoffrey (1992). "The Cominform: Tito's International?". The Historical Journal. 35 (3): 641–663. doi:10.1017/S0018246X00026017. S2CID 163152235.
Tanaka, Yuki (1996). Hidden Horrors: Japanese War Crimes in World War II. Boulder, Colorado: Westview Press. ISBN 978-0-8133-2717-4.
Taylor, A. J. P. (1961). The Origins of the Second World War. London: Hamish Hamilton.
——— (1979). How Wars Begin. London: Hamish Hamilton. ISBN 978-0-241-10017-2.
Taylor, Jay (2009). The Generalissimo: Chiang Kai-shek and the Struggle for Modern China. Cambridge, Massachusetts: Harvard University Press. ISBN 978-0-674-03338-2.
Thomas, Nigel; Andrew, Stephen (1998). German Army 1939–1945 (2): North Africa & Balkans. Oxford: Osprey Publishing. ISBN 978-1-85532-640-8.
Thompson, John Herd; Randall, Stephen J. (2008). Canada and the United States: Ambivalent Allies (4th ed.). Athens, Georgia: University of Georgia Press. ISBN 978-0-8203-3113-3.
Trachtenberg, Marc (1999). A Constructed Peace: The Making of the European Settlement, 1945–1963. Princeton, New Jersey: Princeton University Press. ISBN 978-0-691-00273-6.
Tucker, Spencer C.; Roberts, Priscilla Mary (2004). Encyclopedia of World War II: A Political, Social, and Military History. ABC-CIO. ISBN 978-1-57607-999-7.
Umbreit, Hans (1991). "The Battle for Hegemony in Western Europe". In P. S. Falla (ed.). Germany and the Second World War – Germany's Initial Conquests in Europe. Vol. 2. Oxford: Oxford University Press. pp. 227–326. ISBN 978-0-19-822885-1.
United States Army (1986) [1953]. The German Campaigns in the Balkans (Spring 1941). Washington, D.C.: Department of the Army. Archived from the original on 17 January 2022. Retrieved 17 February 2022.
Waltz, Susan (2002). "Reclaiming and Rebuilding the History of the Universal Declaration of Human Rights". Third World Quarterly. 23 (3): 437–448. doi:10.1080/01436590220138378. JSTOR 3993535. S2CID 145398136.
Ward, Thomas A. (2010). Aerospace Propulsion Systems. Singapore: John Wiley & Sons. ISBN 978-0-470-82497-9.
Watson, William E. (2003). Tricolor and Crescent: France and the Islamic World. Westport, Connecticut: Praeger. ISBN 978-0-275-97470-1.
Weinberg, Gerhard L. (2005). A World at Arms: A Global History of World War II (2nd ed.). Cambridge: Cambridge University Press. ISBN 978-0-521-85316-3.; comprehensive overview with emphasis on diplomacy
Wettig, Gerhard (2008). Stalin and the Cold War in Europe: The Emergence and Development of East-West Conflict, 1939–1953. Lanham, Maryland: Rowman & Littlefield. ISBN 978-0-7425-5542-6.
Wiest, Andrew; Barbier, M. K. (2002). Strategy and Tactics: Infantry Warfare. St Paul, Minnesota: MBI Publishing Company. ISBN 978-0-7603-1401-2.
Williams, Andrew (2006). Liberalism and War: The Victors and the Vanquished. Abingdon & New York: Routledge. ISBN 978-0-415-35980-1.
Wilt, Alan F. (1981). "Hitler's Late Summer Pause in 1941". Military Affairs. 45 (4): 187–191. doi:10.2307/1987464. JSTOR 1987464.
Wohlstetter, Roberta (1962). Pearl Harbor: Warning and Decision. Palo Alto, California: Stanford University Press.
Wolf, Holger C. (1993). "The Lucky Miracle: Germany 1945–1951". In Rudiger Dornbusch; Wilhelm Nölling; Richard Layard (eds.). Postwar Economic Reconstruction and Lessons for the East Today. Cambridge: MIT Press. pp. 29–56. ISBN 978-0-262-04136-2.
Wood, James B. (2007). Japanese Military Strategy in the Pacific War: Was Defeat Inevitable?. Lanham, Maryland: Rowman & Littlefield. ISBN 978-0-7425-5339-2.
Yoder, Amos (1997). The Evolution of the United Nations System (3rd ed.). London & Washington, D.C.: Taylor & Francis. ISBN 978-1-56032-546-8.
Zalampas, Michael (1989). Adolf Hitler and the Third Reich in American magazines, 1923–1939. Bowling Green University Popular Press. ISBN 978-0-87972-462-7.
Zaloga, Steven J. (1996). Bagration 1944: The Destruction of Army Group Centre. Oxford: Osprey Publishing. ISBN 978-1-85532-478-7.
——— (2002). Poland 1939: The Birth of Blitzkrieg. Oxford: Osprey Publishing. ISBN 978-1-84176-408-5.
Zeiler, Thomas W. (2004). Unconditional Defeat: Japan, America, and the End of World War II. Wilmington, Delaware: Scholarly Resources. ISBN 978-0-8420-2991-9.
Zetterling, Niklas; Tamelander, Michael (2009). Bismarck: The Final Days of Germany's Greatest Battleship. Drexel Hill, Pennsylvania: Casemate. ISBN 978-1-935149-04-0.
Further reading
Buchanan, Andrew (7 February 2023). "Globalizing the Second World War". Past & Present (258): 246–281. doi:10.1093/pastj/gtab042. ISSN 0031-2746. also see online review Archived 4 May 2024 at the Wayback Machine
Gerlach, Christian (2024). Conditions of Violence. Walter de Gruyter GmbH & Co KG. ISBN 978-3-1115-6873-7.
External links
show
World War II
at Wikipedia's sister projects
West Point Maps of the European War. Archived 23 March 2019 at the Wayback Machine.
West Point Maps of the Asian-Pacific War. Archived 23 March 2019 at the Wayback Machine.
Atlas of the World Battle Fronts (July 1943 – August 1945)
show
vte
World War II


show
vte
History of World War II by region and country


show
vte
Western world and culture


show
vte
Eastern world and culture


show
Authority control databases 


Categories: World War IIWorld warsConflicts in 1939Conflicts in 1940Conflicts in 1941Conflicts in 1942Conflicts in 1943Conflicts in 1944Conflicts in 1945Late modern EuropeNuclear warfareWars involving AlbaniaWars involving AustraliaWars involving AustriaWars involving BelgiumWars involving BoliviaWars involving BrazilWars involving British IndiaWars involving BulgariaWars involving MyanmarWars involving CambodiaWars involving CanadaWars involving ChileWars involving ColombiaWars involving Costa RicaWars involving CroatiaWars involving CubaWars involving CzechoslovakiaWars involving DenmarkWars involving the Dominican RepublicWars involving EcuadorWars involving EgyptWars involving El SalvadorWars involving EstoniaWars involving EthiopiaWars involving FinlandWars involving FranceWars involving GermanyWars involving GreeceWars involving GuatemalaWars involving HaitiWars involving HondurasWars involving HungaryWars involving IcelandWars involving IndonesiaWars involving ItalyWars involving IranWars involving IraqWars involving JapanWars involving KazakhstanWars involving LaosWars involving LatviaWars involving LebanonWars involving LiberiaWars involving LithuaniaWars involving LuxembourgWars involving MexicoWars involving MongoliaWars involving MontenegroWars involving NepalWars involving NorwayWars involving NicaraguaWars involving PanamaWars involving ParaguayWars involving PeruWars involving PolandWars involving RhodesiaWars involving RomaniaWars involving Saudi ArabiaWars involving SerbiaWars involving SlovakiaWars involving SloveniaWars involving South AfricaWars involving Sri LankaWars involving SyriaWars involving ThailandWars involving the NetherlandsWars involving the PhilippinesWars involving the Republic of ChinaWars involving the Soviet UnionWars involving the United KingdomWars involving the United StatesWars involving UruguayWars involving VenezuelaWars involving VietnamWars involving YugoslaviaWars involving IndiaWars involving New Zealand
    '''
)