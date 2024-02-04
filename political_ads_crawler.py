import json
import os

import requests


def get_next_page(response):
    paging = response.get("paging", {})
    return paging.get("next")


def fetch_data(api_url):
    all_data = []

    while api_url:
        response = requests.get(api_url)

        if response.status_code == 200:
            json_data = response.json()
            data = json_data.get("data", [])
            # Replace "id" with "_id" in each dictionary
            for entry in data:
                entry["_id"] = entry.pop("id", None)

            all_data.extend(data)
            api_url = get_next_page(json_data)
            if api_url:
                print("Moving to the next page...")
            else:
                print("No more pages.")
        else:
            print("Error:", response.status_code)
            break

    return all_data


def main():
    advertisers = [
        # '214827221987263',
        # '55876739776',
        '487445514669670',
        '178362315106',
        '60516116431',
        '107898832590939',
        '111041662264882',
        '102389958091735',
        '295889117124834',
        '179497582061065',
        '251656685576',
        '223117541065037',
        '30575632699',
        '104768355190287',
        '109323929038',
        '107459941935424',
        '102845669064210',
        '728495140691300',
        '470593056405865',
        '197010357446014',
        '90002267161',
        '394570898000897',
        '370583064327',
        '314038193269',
        '1469427909957890',
        '58887737763',
        '106008800769282',
        '103430204491217',
        '114474108677288',
        '356451014434612',
        '424114981002397',
        '298789466930469',
        '317398901621260',
        '944792105610443',
        '101279652413889',
        '711658465662315',
        '384187235387895',
        '2214398435317850',
        '693725074166331',
        '39371299263',
        '361281313901258',
        '134443820058669',
        '34825122262',
        '151864748349113',
        '211685455639198',
        '120343698070515',
        '356448681873897',
        '137778619615350',
        '301612579304',
        '264983260329918',
        '176688316811',
        '1416733788557860',
        '123858471641',
        '55408246161',
        '109787574497667',
        '122074554119',
        '149945438407451',
        '206273352289',
        '117823623864',
        '287724754662359',
        '739115596482745',
        '106834174877753',
        '573004246504627',
        '101198835090246',
        '278117815576023',
        '130631260290858',
        '50309511751',
        '992555574111774',
        '579215965436046',
        '489450987825894',
        '109882498582200',
        '313971562018913',
        '328899600936330',
        '210778132327279',
        '302134090396266',
        '130038285069',
        '120461304659141',
        '1956144064659620',
        '1410403182565680',
        '578342809023884',
        '1269502056393120',
        '496346277123749',
        '107536521911422',
        '103059308644099',
        '1477535869227480',
        '553773474671244',
        '275042429350706',
        '605137899592157',
        '977639539069229',
        '299124538476',
        '315972808450196',
        '115589329891193',
        '370302013674124',
        '252375370791',
        '1817941161841170',
        '460558621177512',
        '849315472073267',
        '105446621928947',
        '113322746709049',
        '100505211433010',
        '107736952362788',
        '157741540937883',
        '278451599256',
        '1104866262972880',
        '100423156141323',
        '101230222584230',
        '397919187215',
        '809013272468388',
        '344542362982337',
        '1736314393286600',
        '213802435698566',
        '252673128998993',
        '110554525653740',
        '206407509818',
        '146713862010620',
        '188866358684457',
        '110477577043297',
        '111210916534',
        '119624098506',
        '102789465825880',
        '442767925822585',
        '257529307701966',
        '733410133337387',
        '206284412716963',
        '139379141293',
        '415472211798220',
        '532219183564760',
        '136248513192',
        '206630153142726',
        '634087193362282',
        '103567498863549',
        '1558359124403840',
        '156199040917285',
        '124152241443',
        '178486018673632',
        '118636354851151',
        '115106741622257',
        '152744724577432',
        '104970479178796',
        '590249011043899',
        '38492561701',
        '120893375974787',
        '105552227912168',
        '163914317133681',
        '495496033796328',
        '159935454034044',
        '114910283210996',
        '291699857688',
        '119598071962341',
        '872454636138704',
        '1458139890966320',
        '153384318085064',
        '574107592700484',
        '297565827101858',
        '108726857444837',
        '597980334012769',
        '187407575190610',
        '267751653384029',
        '109664387308142',
        '419916784781866',
        '589026071265968',
        '121063544248026',
        '135488259638635',
        '1354343051279160',
        '100201752249169',
        '101894271393926',
        '944358442253364',
        '102274002445899',
        '100955509189359',
        '179497582061065',
        # '148026708578836'
    ]

    output_dir = "C:\\Users\\jirip\\Documents\\Developer\\python\\meta_ads_crawler\\political_ads"

    for advertiser_id in advertisers:
        fields = "id,ad_snapshot_url,ad_creation_time,ad_creative_bodies,ad_creative_link_captions,ad_creative_link_descriptions,ad_creative_link_titles,ad_delivery_start_time,ad_delivery_stop_time,bylines,currency,delivery_by_region,demographic_distribution,estimated_audience_size,impressions,languages,page_id,page_name,publisher_platforms,spend,target_locations,target_gender,target_ages,eu_total_reach,beneficiary_payers,age_country_gender_reach_breakdown"
        access_token = "EAALnc8im5MUBO4AZCJJdrzfR2igTbni8Kqo6mwmPiOWI3jlcpP6pnL3S5vGGfKIUpLYL3SSC4myHukWasLPHTALU4psJfwUPheUpSkIM2XJ9umXZA7ZClpYOVYOr2ot8rFE5Y0WYHhzBEBRIzA1LZCElmb1jPqzm2pewYNDj3oMmMXCNii2xIFNuZAK0hJ50NZB3ZCb2ZAI6"
        api_url = f"https://graph.facebook.com/v17.0/ads_archive?search_terms=&ad_type=POLITICAL_AND_ISSUE_ADS&ad_reached_countries=['CZ']&access_token={access_token}&unmask_removed_content=true&search_page_ids={advertiser_id}&fields={fields}&limit=499"

        extracted_data = fetch_data(api_url)

        filename = os.path.join(output_dir, f"data_{advertiser_id}.json")
        with open(filename, "w", encoding='utf-8') as json_file:
            json.dump(extracted_data, json_file, indent=4, ensure_ascii=False)

        print(
            f"All Extracted Data for advertiser {advertiser_id} written to {filename}")


if __name__ == "__main__":
    main()
