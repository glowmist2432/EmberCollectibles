from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


all_registrations = [ 
"YD70 CHX",
"YD70 CHY",
"SG71 OTA",
"SG71 OTF",
"SG22 LTT",
"SG22 LTU",
"SG22 LTV",
"SG22 LTX",
"SG72 NBX",
"SG72 NBY",
"SG72 NBZ",
"SG72 NCA",
"SG72 NCC",
"SG72 NCD",
"SG72 NCE",
"SG72 NCF",
"SG23 ORN",
"SG23 ORO",
"SG23 ORP",
"SG23 ORT",
"SG23 ORU",
"SG23 ORV",
"SG23 ORW",
"SG23 ORX",
"SG24 UHB",
"SG24 UHF",
"SG24 UHL",
"SG24 UHP",
"SG24 UHU",
"SG24 UHY",
"SG24 UJC",
"SG24 UJD",
"SG24 UJE",
"SG24 UJJ",
"SG24 UJK",
"SG24 UJN",
"SG24 UJS",
"SG24 UJW",
"SG25 HXW",
"SG25 HXX",
"SG25 HXY",
"SG25 HXZ",
"SG25 HYA",
"SG25 HYB",
"SG25 HYC",
"SG25 HYF",
"SG25 HYH",
"SG25 HYJ",
"SG25 HYK",
"SG25 HYL",
"SG25 HYM",
"SG25 HYN",
"SG25 HYO",
"SG25 HYP",
"SG25 HYR",
"SG25 HYS",
"SG25 HYT",
"SG25 HYU",
"SG25 HYV",
"SG25 HYW",
"SG25 HYX",
"SG25 HYY",
"SG25 HYZ",
"SG25 HZA",
"SG25 HZB",
"SG25 HZC",
"SG25 HZD",
"SG25 HZE",
"SG25 HZF",
"SG25 HZH",
"SG25 HZJ",
"SG25 HZK",
"SG25 HZL",
"SG25 HZM",
"SG25 HZN",
"SG25 HZP",
"SG25 HZR",
"SG25 HZS",
"SJ26 XOU",
"SJ26 XOV",
"SJ26 XOW",
"SJ26 XOX",
"SJ26 XOY",
"SJ26 XOZ",
"SJ26 XPA",
"SJ26 XPB",
"SJ26 XPC",
"SJ26 XPD",
"SJ26 XPE",
"SJ26 XPF",
"SJ26 XPG",
"SJ26 XPH",
"SJ26 XPK",
"SJ26 XPL",
"SJ26 XPM",
"SJ26 XPN",
"SJ26 XPO",
"SJ26 XPP",
"SJ26 XPR",
"SJ26 XPS",
"SJ26 XPT",
"SJ26 XPU",
"SJ26 XPV",
"SJ26 XPW",
"SJ26 XPX",
"SJ26 XPY",
"SJ26 XPZ",
"SJ26 XRA",
"SJ26 XRB",
"SJ26 XRC",
"SJ26 XRD",
"SJ26 XRE",
"SJ26 XRF",
"SJ26 XRG",
"SJ26 XRH",
"SJ26 XRK",
"SJ26 XRL",
"SJ26 XRM"

]


collected_registrations = []


all_collectibles = [
    {
       "id": "1_reg",
        "name": "First Bus",
        "image": "images/first_bus_award.png",
        "description": "Ride your first bus." 
    },

    {
        "id": "5_reg",
        "name": "Five Buses",
        "image": "images/firebus.png",
        "description": "Ride five different buses." 
    },

    {
        "id": "25_reg",
        "name": "Twenty Five Buses",
        "image": "images/silver_bus.png",
        "description": "Ride twenty five different buses." 
    },

    {
        "id": "50_reg",
        "name": "Fifty Buses",
        "image": "images/gold_bus.png",
        "description": "Ride fifty different buses." 
    },

    {
        "id": "stirling_st-andrews",
        "name": "Stirling to St Andrews",
        "image": "images/str_sta_journey.png",
        "description": "Ride a bus on the Stirling to St. Andrews route.",
        "journey" : "e99" 
    }, 

    {
        "id": "aberdeen_dundee",
        "name": "Aberdeen to Dundee",
        "image": "images/abn_dnd_journey.png",
        "description": "Ride a bus on the Dundee to Edinburgh route" ,
        "journey" : "e11"
    }, 

    {
        "id": "glasgow_fort-william",
        "name": "Glasgow to Fort William",
        "image": "images/gla_fw_journey.png",
        "description": "Ride a bus on the Glasgow to Fort William route",
        "journey" : "e5" 
    },

    {
        "id": "oban_edinburgh",
        "name": "Oban to Edinburgh",
        "image": "images/oban_edi_journey.png",
        "description": "Ride a bus on the Oban to Edinburgh route",
        "journey" : "e15" 
    }



]

collected_collectibles = []



completed_journeys = []


journeys = [

    {
        "id": "e1",
        "name" : "Aberdeen and Edinburgh"
    },

    {
        "id": "e3",
        "name" : "Dundee and Glasgow"
    },

    {
        "id": "e4",
        "name" : "Edinburgh and Fort William"
    },

    {
        "id" : "e4x",
        "name" : "Edinburgh and Fort William"
    },

    {
        "id" : "e5",
        "name" : "Fort William and Glasgow"
    },

    {
        "id" : "e6",
        "name" : "Inverness and Thurso"
    },

    {
        "id" : "e7",
        "name" : "Aberdeen and Inverness"
    },

    {
        "id" : "e8",
        "name" : "Glasgow and Inverness"
    },

    {
        "id" : "e9",
        "name" : "Edinburgh and Inverness"
    },

    {
        "id" : "e10",
        "name" : "Dundee and Dundee"
    },

    {
        "id" : "e11",
        "name" : "Aberdeen and Dundee"
    },

    {
        "id" : "e12",
        "name" : "Carmyle and Glasgow"
    },

    {
        "id" : "e14",
        "name" : "Inverness and Oban"
    },

    {
        "id" : "e15",
        "name" : "Edinburgh and Oban"
    },

    {
        "id" : "e16",
        "name" : "Glasgow and Oban"
    },

    {
        "id" : "e17",
        "name" : "Aberdeen and Perth"
    },

    {
        "id" : "e18",
        "name" : "Inverness and Ullapool"
    },

    {
        "id" : "e19",
        "name" : "Edinburgh Airport and Livingston"
    },

    {
        "id" : "e20",
        "name" : "Edinburgh Airport and Glasgow"
    },

    {
        "id" : "e99",
        "name" : "Stirling and St Andrews"
    }

]





def check_collectibles():

    # First journey
    if len(collected_registrations) >= 1:
        if "1_reg" not in collected_collectibles:
            collected_collectibles.append("1_reg")

    # Five registrations
    if len(collected_registrations) >= 5:
        if "5_reg" not in collected_collectibles:
            collected_collectibles.append("5_reg")

    # 25 registrations
    if len(collected_registrations) >= 25:
        if "25_reg" not in collected_collectibles:
            collected_collectibles.append("25_reg")

    # 50 reg
    if len(collected_registrations) >= 50:
        if "50_reg" not in collected_collectibles:
            collected_collectibles.append("50_reg")


    for collectible in all_collectibles:
        if "journey" not in collectible:
            continue

        required_journey = collectible["journey"]

        # Check whether the user has completed that journey
        if required_journey in completed_journeys:

            if collectible["id"] not in collected_collectibles:
                collected_collectibles.append(collectible["id"]) 



@app.route("/")
def home():
    return render_template(
        "index.html",
        journeys=journeys,
        collected_registrations=collected_registrations,
        collected_collectibles=collected_collectibles,
        completed_journeys=completed_journeys
    )

@app.route("/<page>")
def get_page(page):
    return render_template(f"{page}.html")



@app.route("/submit-journey", methods=["POST"])
def submit_journey():

    data = request.get_json()

    registration = data.get("registration")
    journey = data.get("journey")

    print("Registration:", registration)
    print("Journey:", journey)

    # Do whatever processing/database work you need here
    if not registration or not journey:
        return jsonify({"error": "Please enter a registration and select a journey."}), 400

    registration = registration.upper().strip()

    if registration not in all_registrations:
        return jsonify({"error": "This registration plate is not recognised."}), 400

    if registration not in collected_registrations:
        collected_registrations.append(registration)
        message = f"{registration} has been added to your collection!"
    else:
        message = f"{registration} is already in your collection."


    if journey not in completed_journeys:
        completed_journeys.append(journey)

    check_collectibles()

    return jsonify({
        "message": message,
        "collected": collected_registrations
    })


@app.route("/registrations")
def registrations():
    sorted_registrations = sorted(
        all_registrations,
        key=lambda plate: plate not in collected_registrations
    )

    return render_template(
        "registrations.html",
        registrations=sorted_registrations,
        collected=collected_registrations
    )


@app.route("/collectibles")
def collectibles():
    return render_template(
        "collectibles.html",
        collectibles=all_collectibles,
        collected=collected_collectibles
    )



if __name__ == "__main__":
    app.run(debug=True)