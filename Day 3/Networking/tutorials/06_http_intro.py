import requests
import json
import time
import os
from urllib.parse import urljoin
import base64

class RESTApiClient:
    """A generic REST API client implementation."""
    
    def __init__(self, base_url, auth=None, headers=None):
        """
        Initialize the REST API client.
        
        Args:
            base_url (str): The base URL for the API
            auth (tuple, optional): Basic auth credentials (username, password)
            headers (dict, optional): Default headers to send with each request
        """
        self.base_url = base_url
        self.auth = auth
        
        # Default headers
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        # Update with custom headers if provided
        if headers:
            self.headers.update(headers)
        
        # Create a session for connection pooling and consistent headers
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
        if auth:
            self.session.auth = auth
    
    def get(self, endpoint, params=None):
        """
        Make a GET request to the API.
        
        Args:
            endpoint (str): The API endpoint (will be joined with base_url)
            params (dict, optional): Query parameters to include
            
        Returns:
            dict: The JSON response
        """
        url = urljoin(self.base_url, endpoint)
        response = self.session.get(url, params=params)
        response.raise_for_status()  # Raise exception for 4XX/5XX responses
        return response.json()
    
    def post(self, endpoint, data=None, json_data=None):
        """
        Make a POST request to the API.
        
        Args:
            endpoint (str): The API endpoint
            data (dict, optional): Form data to send
            json_data (dict, optional): JSON data to send
            
        Returns:
            dict: The JSON response
        """
        url = urljoin(self.base_url, endpoint)
        response = self.session.post(url, data=data, json=json_data)
        response.raise_for_status()
        return response.json()
    
    def put(self, endpoint, data=None, json_data=None):
        """
        Make a PUT request to the API.
        
        Args:
            endpoint (str): The API endpoint
            data (dict, optional): Form data to send
            json_data (dict, optional): JSON data to send
            
        Returns:
            dict: The JSON response
        """
        url = urljoin(self.base_url, endpoint)
        response = self.session.put(url, data=data, json=json_data)
        response.raise_for_status()
        return response.json()
    
    def delete(self, endpoint, params=None):
        """
        Make a DELETE request to the API.
        
        Args:
            endpoint (str): The API endpoint
            params (dict, optional): Query parameters to include
            
        Returns:
            dict: The JSON response (if any)
        """
        url = urljoin(self.base_url, endpoint)
        response = self.session.delete(url, params=params)
        response.raise_for_status()
        
        # Some DELETE endpoints return no content
        if response.status_code == 204:
            return {"status": "success", "message": "Resource deleted"}
        
        try:
            return response.json()
        except ValueError:
            return {"status": "success", "message": "Resource deleted", "content": response.text}
    
    def handle_pagination(self, endpoint, params=None, results_key='results', next_page_key='next'):
        """
        Handle paginated API responses.
        
        Args:
            endpoint (str): The API endpoint
            params (dict, optional): Query parameters
            results_key (str): The JSON key containing results in each response
            next_page_key (str): The JSON key containing the next page URL
            
        Returns:
            list: Combined results from all pages
        """
        url = urljoin(self.base_url, endpoint)
        all_results = []
        
        while url:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Extract the results from this page
            if results_key in data:
                all_results.extend(data[results_key])
            
            # Get the next page URL, if any
            url = data.get(next_page_key)
            
            # Clear params for subsequent requests, as they're typically included in the next_page URL
            params = None
            
            # Optional rate limiting
            time.sleep(0.1)
        
        return all_results


# Example usage of the generic REST API client
def demonstrate_generic_rest_client():
    """Demonstrate using the generic REST API client with a public API."""
    print("GENERIC REST API CLIENT DEMONSTRATION")
    print("-------------------------------------")
    
    # Initialize client with JSONPlaceholder API (free test API)
    client = RESTApiClient("https://jsonplaceholder.typicode.com/")
    
    # GET request - fetch all posts
    try:
        print("\n1. GET REQUEST - Fetch posts")
        posts = client.get("posts")
        print(f"   Retrieved {len(posts)} posts")
        print(f"   First post: {json.dumps(posts[0], indent=2)}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # GET request with filtering
    try:
        print("\n2. GET REQUEST WITH PARAMETERS - Filter posts by user")
        user_posts = client.get("posts", params={"userId": 1})
        print(f"   Retrieved {len(user_posts)} posts for user 1")
        print(f"   Sample post: {json.dumps(user_posts[0], indent=2)}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # POST request - create a new post
    try:
        print("\n3. POST REQUEST - Create a new post")
        new_post_data = {
            "title": "New Post from Python",
            "body": "This is a post created using our Python REST API client",
            "userId": 1
        }
        new_post = client.post("posts", json_data=new_post_data)
        print(f"   Created post with ID: {new_post['id']}")
        print(f"   Post details: {json.dumps(new_post, indent=2)}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # PUT request - update a post
    try:
        print("\n4. PUT REQUEST - Update a post")
        update_data = {
            "id": 1,
            "title": "Updated Post Title",
            "body": "Updated post body text",
            "userId": 1
        }
        updated_post = client.put("posts/1", json_data=update_data)
        print(f"   Updated post: {json.dumps(updated_post, indent=2)}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # DELETE request - delete a post
    try:
        print("\n5. DELETE REQUEST - Delete a post")
        delete_result = client.delete("posts/1")
        print(f"   Delete result: {json.dumps(delete_result, indent=2)}")
    except Exception as e:
        print(f"   Error: {e}")


demonstrate_generic_rest_client()