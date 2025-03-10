import csv
import ollama

def query_ollama(question, plant):
    """Query Ollama with a question about a specific plant."""
    prompt = question.replace("[]", plant)
    response = ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

def generate_csv(plants, questions, output_file='plant_data.csv'):
    """Generate a CSV file with responses from Ollama."""
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write header
        headers = ['Plant'] + questions
        writer.writerow(headers)
        
        # Query for each plant
        for plant in plants:
            row = [plant]
            print("Starting "+plant)
            for question in questions:
                answer = query_ollama(question, plant)
                row.append(answer)
            writer.writerow(row)
    
    print(f"CSV file '{output_file}' created successfully.")

if __name__ == "__main__":
    # List of plants
    plants = [
      "Daylilies", "Irises", "Roses", "Sempervivum", "Lilies", "Hostas", "Dahlias", "Peonies", "Daffodils", "Tomatoes",
      "Abelias", "Abutilons", "Adeniums", "Aeoniums", "Agapanthus", "Agaves", "Aglaonemas", "Air Plants", "Aloes", "Amaryllis",
      "Amorphophallus", "Angel's Trumpets", "Anise Hyssops", "Anthuriums", "Apples", "Apricots", "Arborvitaes", "Arisaemas",
      "Artichokes", "Arums", "Asparagus", "Asters", "Astilbes", "Astragaluses", "Baby's Breaths", "Bananas", "Baptisias",
      "Barberries", "Basils", "Beans", "Beautyberries", "Bee Balms", "Beets", "Begonias", "Bellflowers", "Black Eyed Susans",
      "Blanket Flowers", "Bleeding Hearts", "Blood Lilies", "Bluebeards", "Bluestem Grasses", "Bougainvilleas", "Brassicas",
      "Butterfly Bushes", "Butterworts", "Caladiums", "Calibrachoas", "Callas", "Camellias", "Cannas", "Cantaloupes",
      "Cape Lilies", "Cape Primroses", "Carrots", "Castor Beans", "Catmints", "Celeries", "Chickweed", "Chives", "Chlorophytums",
      "Chollas", "Cilantros", "Citrus Fruits", "Clematis", "Clivias", "Colchicums", "Coleus", "Columbines", "Coneflowers",
      "Consolidas", "Coral Bells", "Corn", "Cosmos", "Crassulas", "Crepe Myrtles", "Crinums", "Crocosmias", "Crocus", "Crotons",
      "Cucumbers", "Culinary Sages", "Currants And Gooseberries", "Dead Nettles", "Delphiniums", "Dianthus", "Dieffenbachias",
      "Dills", "Dogwoods", "Dracontiums", "Dudleyas", "Echeverias", "Eggplants", "Elephant Ears (Alocasia)", 
      "Elephant Ears (Colocasia)", "Elephant Ears (Xanthosoma)", "Epiphyllum", "Erodiums", "Erythroniums", "Eupatoriums",
      "Euphorbias", "False Bananas", "Figs", "Foamflowers", "Foamy Bells", "Foxgloves", "Freesias", "Fritillarias", "Fuchsias",
      "Garden Nasturtiums", "Gardenias", "Garlic", "Gayfeathers", "Geraniums", "Ginger Lilies", "Gingers", "Gladiolus",
      "Goldenrods", "Gourds, Squashes And Pumpkins", "Grape Hyacinths", "Grapes", "Heavenly Bamboos", "Hellebores", "Hibiscus",
      "Homalomenas", "Honeysuckles", "Hoyas", "Hyacinths", "Hydrangeas", "Ilex", "Joe Pye Weed", "Jujubes", "Kalanchoes",
      "Lamb's Ears", "Lantanas", "Lavenders", "Leeks", "Lettuces", "Ligularias", "Lilacs", "Lilies Of The Valley", "Lions Tail",
      "Liriopes", "Living Stones", "Lotuses", "Magnolias", "Maianthemums", "Mammillarias", "Mangoes", "Marjorams", "Melaleucas",
      "Milkweeds", "Mints", "Mirabilis", "Mock Oranges", "Monsteras", "Morning Glories", "Nicotianas", "Ninebarks", "Nymphaeas",
      "Oenotheras", "Okra", "Oleanders", "Onions", "Oreganos", "Orostachys", "Pachypodiums", "Parsleys", "Parsnips", "Pawpaws",
      "Peace Lilies", "Peaches", "Pears", "Peas", "Pecans", "Pelargoniums", "Penstemons", "Peppers", "Persimmons", 
      "Peruvian Lilies", "Petunias", "Philodendrons", "Phloxes", "Pinellias", "Pitcher Plants", "Platycodons", "Plumerias",
      "Plums", "Pomegranates", "Poppies", "Potatoes", "Prickly Pears", "Primroses", "Radishes", "Rain Lilies", "Rhododendrons",
      "Rhubarbs", "Rockroses", "Roses Of Sharon", "Rosularias", "Rubus", "Salvias", "Sauromatums", "Schlumbergeras", "Sedges",
      "Sedums", "Shasta Daisies", "Shell Flowers (Pavonia)", "Silphiums", "Sisyrinchiums", "Smoketrees", "Snake Plants",
      "Snowdrops", "Southern Peas", "Spider Lilies", "Spinaches", "Spiraeas", "Spruces", "Strawberries", "Sunflowers",
      "Sunroots", "Surprise Lilies (Lycoris)", "Sweet Cherries", "Sweet Potatoes", "Swiss Chards", "Syngoniums", "Tarragons",
      "Thymes", "Tickseeds", "Toad Lilies", "Torch Lilies", "Tradescantias", "Trilliums", "Tropical Hibiscuses", "Tulips",
      "Turnips", "Typhoniums", "Uvularias", "Veronicas", "Viburnums", "Violas", "Watermelons", "Wild Gingers", "Wisterias",
      "Witch Hazels", "Wood Sorrels", "Yarrows"
    ]   
    # plants = ["Daylilies"]
    
     # List of questions
    questions = ["How much sunlight does [] need?",
      "How often should I water []?",
      "How should I water []?",
      "How much should I water []?"
      "What type of soil does [] need?",
      "How big of a pot does [] need?",
      "How big will [] be?",
      "What is the ideal temperature range for []?",
      "Should I use tap water, distilled water, or filtered water for []?",
      "How fast does [] grow?",
      "What size pot should I use for []?",
      "What are the signs that [] needs repotting?",
      "Does [] need support, like a moss pole or stake?",
      "How often should I fertilize []?",
      "What type of fertilizer should I use for []?",
      "What are signs that [] is over-fertilized?",
      "Should I fertilize [] only during growing seasons?",
      "What common pests affect []?",
      "How do I get rid of the pests that affect []?",
      "Is it safe to place [] near an air conditioner or heater?",
      "Can I put [] in the bathroom/bedroom/kitchen?",
      "Will [] be okay if I keep it outside?",
      "Is [] toxic to pets or children?",
      "Does [] go dormant in certain seasons?",
      "What are signs that [] is stressed or unhealthy?",
      "Can [] be kept in water instead of soil (hydroponics)?"
    ]
    
    generate_csv(plants, questions)
