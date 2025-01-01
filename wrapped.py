import requests
import blackboxprotobuf

def get_spotify_wrapped_data(bearer_token: str) -> dict:
    url = "https://spclient.wg.spotify.com/campaigns-service/v1/campaigns/wrapped/consumer"
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        message, typedef = blackboxprotobuf.protobuf_to_json(response.content)
        return message
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch Spotify data: {str(e)}")
    except Exception as e:
        raise Exception(f"Failed to decode protobuf data: {str(e)}")

def save(data, output_file: str = "spotify_wrapped.json"):
    with open(output_file, 'w') as f:
        f.write(data)

def main():
    bearer_token = "your spotify token"
    try:
        data = get_spotify_wrapped_data(bearer_token)
        save(data)
        print("Successfully saved Spotify Wrapped data to spotify_wrapped.json")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()