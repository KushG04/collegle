import json

colleges = {
    "Princeton University": {
        "ranking": 1,
        "acceptance_rate": 6,
        "type": "Private",
        "state": "NJ"
    },
    "Massachusetts Institute of Technology": {
        "ranking": 2,
        "acceptance_rate": 4,
        "type": "Private",
        "state": "MA"
    },
    "Harvard University": {
        "ranking": 3,
        "acceptance_rate": 3,
        "type": "Private",
        "state": "MA"
    },
    "Stanford University": {
        "ranking": 3,
        "acceptance_rate": 4,
        "type": "Private",
        "state": "CA"
    },
    "Yale University": {
        "ranking": 5,
        "acceptance_rate": 5,
        "type": "Private",
        "state": "CT"
    },
    "University of Pennsylvania": {
        "ranking": 6,
        "acceptance_rate": 7,
        "type": "Private",
        "state": "PA"
    },
    "California Institute of Technology": {
        "ranking": 7,
        "acceptance_rate": 3,
        "type": "Private",
        "state": "CA"
    },
    "Duke University": {
        "ranking": 7,
        "acceptance_rate": 6,
        "type": "Private",
        "state": "NC"
    },
    "Brown University": {
        "ranking": 9,
        "acceptance_rate": 5,
        "type": "Private",
        "state": "RI"
    },
    "John Hopkins University": {
        "ranking": 9,
        "acceptance_rate": 7,
        "type": "Private",
        "state": "MD"
    },
    "Northwestern University": {
        "ranking": 9,
        "acceptance_rate": 7,
        "type": "Private",
        "state": "IL"
    },
    "Columbia University": {
        "ranking": 12,
        "acceptance_rate": 4,
        "type": "Private",
        "state": "NY"
    },
    "Cornell University": {
        "ranking": 12,
        "acceptance_rate": 7,
        "type": "Private",
        "state": "NY"
    },
    "University of Chicago": {
        "ranking": 12,
        "acceptance_rate": 5,
        "type": "Private",
        "state": "IL"
    },
    "University of California, Berkeley": {
        "ranking": 15,
        "acceptance_rate": 11,
        "type": "Public",
        "state": "CA"
    },
    "University of California, Los Angeles": {
        "ranking": 15,
        "acceptance_rate": 9,
        "type": "Public",
        "state": "CA"
    },
    "Rice University": {
        "ranking": 17,
        "acceptance_rate": 9,
        "type": "Private",
        "state": "TX"
    },
    "Dartmouth College": {
        "ranking": 18,
        "acceptance_rate": 6,
        "type": "Private",
        "state": "NH"
    },
    "Vanderbilt University": {
        "ranking": 18,
        "acceptance_rate": 7,
        "type": "Private",
        "state": "TN"
    },
    "University of Notre Dame": {
        "ranking": 20,
        "acceptance_rate": 13,
        "type": "Private",
        "state": "IN"
    },
    "University of Michigan--Ann Arbor": {
        "ranking": 21,
        "acceptance_rate": 18,
        "type": "Public",
        "state": "MI"
    },
    "Georgetown University": {
        "ranking": 22,
        "acceptance_rate": 12,
        "type": "Private",
        "state": "DC"
    },
    "University of North Carolina at Chapel Hill": {
        "ranking": 22,
        "acceptance_rate": 17,
        "type": "Public",
        "state": "NC"
    },
    "Carnegie Mellon University": {
        "ranking": 24,
        "acceptance_rate": 11,
        "type": "Private",
        "state": "PA"
    },
    "Emory University": {
        "ranking": 24,
        "acceptance_rate": 11,
        "type": "Private",
        "state": "GA"
    },
    "University of Virginia": {
        "ranking": 24,
        "acceptance_rate": 19,
        "type": "Public",
        "state": "VA"
    },
    "Washington University in St. Louis": {
        "ranking": 24,
        "acceptance_rate": 12,
        "type": "Private",
        "state": "MO"
    },
    "University of California, Davis": {
        "ranking": 28,
        "acceptance_rate": 37,
        "type": "Public",
        "state": "CA"
    },
    "University of California, San Diego": {
        "ranking": 28,
        "acceptance_rate": 24,
        "type": "Public",
        "state": "CA"
    },
    "University of Florida": {
        "ranking": 28,
        "acceptance_rate": 23,
        "type": "Public",
        "state": "FL"
    },
    "University of Southern California": {
        "ranking": 28,
        "acceptance_rate": 12,
        "type": "Private",
        "state": "CA"
    },
    "University of Texas at Austin": {
        "ranking": 32,
        "acceptance_rate": 31,
        "type": "Public",
        "state": "TX"
    },
    "Georgia Institute of Technology": {
        "ranking": 33,
        "acceptance_rate": 17,
        "type": "Public",
        "state": "GA"
    },
    "University of California, Irvine": {
        "ranking": 33,
        "acceptance_rate": 21,
        "type": "Public",
        "state": "CA"
    },
    "New York University": {
        "ranking": 35,
        "acceptance_rate": 12,
        "type": "Private",
        "state": "NY"
    },
    "University of California, Santa Barbara": {
        "ranking": 35,
        "acceptance_rate": 26,
        "type": "Public",
        "state": "CA"
    },
    "University of Illinois Urbana-Champaign": {
        "ranking": 35,
        "acceptance_rate": 45,
        "type": "Public",
        "state": "IL"
    },
    "University of Wisconsin--Madison": {
        "ranking": 35,
        "acceptance_rate": 49,
        "type": "Public",
        "state": "WI"
    },
    "Boston College": {
        "ranking": 39,
        "acceptance_rate": 17,
        "type": "Private",
        "state": "MA"
    },
    "Rutgers University--New Brunswick": {
        "ranking": 40,
        "acceptance_rate": 66,
        "type": "Public",
        "state": "NJ"
    },
    "Tufts University": {
        "ranking": 40,
        "acceptance_rate": 10,
        "type": "Private",
        "state": "MA"
    },
    "University of Washington": {
        "ranking": 40,
        "acceptance_rate": 48,
        "type": "Public",
        "state": "WA"
    },
    "Boston University": {
        "ranking": 43,
        "acceptance_rate": 14,
        "type": "Private",
        "state": "MA"
    },
    "The Ohio State University": {
        "ranking": 43,
        "acceptance_rate": 53,
        "type": "Public",
        "state": "OH"
    },
    "Purdue University--Main Campus": {
        "ranking": 43,
        "acceptance_rate": 53,
        "type": "Public",
        "state": "IN"
    },
    "University of Maryland, College Park": {
        "ranking": 46,
        "acceptance_rate": 45,
        "type": "Public",
        "state": "MD"
    },
    "Lehigh University": {
        "ranking": 47,
        "acceptance_rate": 37,
        "type": "Private",
        "state": "PA"
    },
    "Texas A&M University": {
        "ranking": 47,
        "acceptance_rate": 63,
        "type": "Public",
        "state": "TX"
    },
    "University of Georgia": {
        "ranking": 47,
        "acceptance_rate": 43,
        "type": "Public",
        "state": "GA"
    },
    "University of Rochester": {
        "ranking": 47,
        "acceptance_rate": 39,
        "type": "Private",
        "state": "NY"
    },
    "Virginia Tech": {
        "ranking": 47,
        "acceptance_rate": 57,
        "type": "Public",
        "state": "VA"
    },
    "Wake Forest University": {
        "ranking": 47,
        "acceptance_rate": 21,
        "type": "Private",
        "state": "NC"
    },
    "Case Western Reserve University": {
        "ranking": 53,
        "acceptance_rate": 27,
        "type": "Private",
        "state": "OH"
    },
    "Florida State University": {
        "ranking": 53,
        "acceptance_rate": 25,
        "type": "Public",
        "state": "FL"
    },
    "Northeastern University": {
        "ranking": 53,
        "acceptance_rate": 7,
        "type": "Private",
        "state": "MA"
    },
    "University of Minnesota, Twin Cities": {
        "ranking": 53,
        "acceptance_rate": 75,
        "type": "Public",
        "state": "MN"
    },
    "William & Mary": {
        "ranking": 53,
        "acceptance_rate": 33,
        "type": "Public",
        "state": "VA"
    },
    "Stony Brook University--SUNY": {
        "ranking": 58,
        "acceptance_rate": 49,
        "type": "Public",
        "state": "NY"
    },
    "University of Connecticut": {
        "ranking": 58,
        "acceptance_rate": 55,
        "type": "Public",
        "state": "CT"
    },
    "Brandeis University": {
        "ranking": 60,
        "acceptance_rate": 39,
        "type": "Private",
        "state": "MA"
    },
    "Michigan State University": {
        "ranking": 60,
        "acceptance_rate": 88,
        "type": "Public",
        "state": "MI"
    },
    "North Carolina State University": {
        "ranking": 60,
        "acceptance_rate": 47,
        "type": "Public",
        "state": "NC"
    },
    "The Pennsylvania State University--University Park": {
        "ranking": 60,
        "acceptance_rate": 55,
        "type": "Public",
        "state": "PA"
    },
    "Rensselaer Polytechnic Institute": {
        "ranking": 60,
        "acceptance_rate": 65,
        "type": "Private",
        "state": "NY"
    },
    "Santa Clara University": {
        "ranking": 60,
        "acceptance_rate": 52,
        "type": "Private",
        "state": "CA"
    },
    "University of California, Merced": {
        "ranking": 60,
        "acceptance_rate": 89,
        "type": "Public",
        "state": "CA"
    },
    "George Washington University": {
        "ranking": 67,
        "acceptance_rate": 49,
        "type": "Private",
        "state": "DC"
    },
    "Syracuse University": {
        "ranking": 67,
        "acceptance_rate": 52,
        "type": "Private",
        "state": "NY"
    },
    "University of Massachusetts--Amherst": {
        "ranking": 67,
        "acceptance_rate": 64,
        "type": "Public",
        "state": "MA"
    },
    "University of Miami": {
        "ranking": 67,
        "acceptance_rate": 19,
        "type": "Private",
        "state": "FL"
    },
    "University of Pittsburgh": {
        "ranking": 67,
        "acceptance_rate": 49,
        "type": "Public",
        "state": "PA"
    },
    "Villanova University": {
        "ranking": 67,
        "acceptance_rate": 23,
        "type": "Private",
        "state": "PA"
    },
    "Binghamton University--SUNY": {
        "ranking": 73,
        "acceptance_rate": 42,
        "type": "Public",
        "state": "NY"
    },
    "Indiana University--Bloomington": {
        "ranking": 73,
        "acceptance_rate": 82,
        "type": "Public",
        "state": "IN"
    },
    "Tulane University": {
        "ranking": 73,
        "acceptance_rate": 11,
        "type": "Private",
        "state": "LA"
    },
    "Colorado School of Mines": {
        "ranking": 76,
        "acceptance_rate": 58,
        "type": "Public",
        "state": "CO"
    },
    "Pepperdine University": {
        "ranking": 76,
        "acceptance_rate": 49,
        "type": "Private",
        "state": "CA"
    },
    "Stevens Institute of Technology": {
        "ranking": 76,
        "acceptance_rate": 46,
        "type": "Private",
        "state": "NJ"
    },
    "University at Buffalo--SUNY": {
        "ranking": 76,
        "acceptance_rate": 68,
        "type": "Public",
        "state": "NY"
    },
    "University of California, Riverside": {
        "ranking": 76,
        "acceptance_rate": 69,
        "type": "Public",
        "state": "CA"
    },
    "University of Delaware": {
        "ranking": 76,
        "acceptance_rate": 74,
        "type": "Public",
        "state": "DE"
    },
    "Rutgers University--Newark": {
        "ranking": 82,
        "acceptance_rate": 74,
        "type": "Public",
        "state": "NJ"
    },
    "University of California, Santa Cruz": {
        "ranking": 82,
        "acceptance_rate": 47,
        "type": "Public",
        "state": "CA"
    },
    "University of Illinois--Chicago": {
        "ranking": 82,
        "acceptance_rate": 79,
        "type": "Public",
        "state": "IL"
    },
    "Worcester Polytechnic Institute": {
        "ranking": 82,
        "acceptance_rate": 57,
        "type": "Private",
        "state": "MA"
    },
    "Clemson University": {
        "ranking": 86,
        "acceptance_rate": 43,
        "type": "Public",
        "state": "SC"
    },
    "Marquette University": {
        "ranking": 86,
        "acceptance_rate": 87,
        "type": "Private",
        "state": "WI"
    },
    "New Jersey Institute of Technology": {
        "ranking": 86,
        "acceptance_rate": 66,
        "type": "Public",
        "state": "NJ"
    },
    "Fordham University": {
        "ranking": 89,
        "acceptance_rate": 54,
        "type": "Private",
        "state": "NY"
    },
    "Southern Methodist University": {
        "ranking": 89,
        "acceptance_rate": 52,
        "type": "Private",
        "state": "TX"
    },
    "Temple University": {
        "ranking": 89,
        "acceptance_rate": 80,
        "type": "Public",
        "state": "PA"
    },
    "University of South Florida": {
        "ranking": 89,
        "acceptance_rate": 44,
        "type": "Public",
        "state": "FL"
    },
    "Auburn University": {
        "ranking": 93,
        "acceptance_rate": 44,
        "type": "Public",
        "state": "AL"
    },
    "Baylor University": {
        "ranking": 93,
        "acceptance_rate": 46,
        "type": "Private",
        "state": "TX"
    },
    "Gonzaga University": {
        "ranking": 93,
        "acceptance_rate": 70,
        "type": "Private",
        "state": "WA"
    },
    "Loyola Marymount University": {
        "ranking": 93,
        "acceptance_rate": 41,
        "type": "Private",
        "state": "CA"
    },
    "University of Iowa": {
        "ranking": 93,
        "acceptance_rate": 86,
        "type": "Public",
        "state": "IA"
    },
    "Drexel University": {
        "ranking": 98,
        "acceptance_rate": 80,
        "type": "Private",
        "state": "PA"
    },
    "Illinois Institute of Technology": {
        "ranking": 98,
        "acceptance_rate": 61,
        "type": "Private",
        "state": "IL"
    },
    "Rochester Institute of Technology": {
        "ranking": 98,
        "acceptance_rate": 67,
        "type": "Private",
        "state": "NY"
    }
}

with open('colleges.json', 'w') as c:
    json.dump(colleges, c)

print("colleges.json file created")