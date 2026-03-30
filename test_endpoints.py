#!/usr/bin/env python3
"""
Test script for HexStrike AI SSE and HTTP MCP endpoints
"""

import requests
import json
import time

def test_http_mcp():
    """Test HTTP MCP endpoint"""
    print("🔧 Testing HTTP MCP endpoint...")
    
    # Test initialize
    try:
        response = requests.post('http://localhost:8888/mcp', 
                               json={
                                   'jsonrpc': '2.0', 
                                   'id': 1, 
                                   'method': 'initialize', 
                                   'params': {
                                       'protocolVersion': '2024-11-05',
                                       'capabilities': {},
                                       'clientInfo': {
                                           'name': 'test-client',
                                           'version': '1.0.0'
                                       }
                                   }
                               },
                               headers={'Content-Type': 'application/json'},
                               timeout=5)
        
        print(f"✅ Initialize Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Initialize Response: {json.dumps(data, indent=2)}")
        else:
            print(f"❌ Initialize Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Initialize Connection Error: {e}")
    
    # Test tools/list
    try:
        response = requests.post('http://localhost:8888/mcp', 
                               json={
                                   'jsonrpc': '2.0', 
                                   'id': 2, 
                                   'method': 'tools/list'
                               },
                               headers={'Content-Type': 'application/json'},
                               timeout=5)
        
        print(f"✅ Tools List Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Tools List Response: {json.dumps(data, indent=2)}")
        else:
            print(f"❌ Tools List Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Tools List Connection Error: {e}")
    
    # Test tool call
    try:
        response = requests.post('http://localhost:8888/mcp', 
                               json={
                                   'jsonrpc': '2.0', 
                                   'id': 3, 
                                   'method': 'tools/call',
                                   'params': {
                                       'name': 'hexstrike_scan',
                                       'arguments': {
                                           'target': '192.168.1.1',
                                           'scan_type': 'port'
                                       }
                                   }
                               },
                               headers={'Content-Type': 'application/json'},
                               timeout=5)
        
        print(f"✅ Tool Call Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Tool Call Response: {json.dumps(data, indent=2)}")
        else:
            print(f"❌ Tool Call Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Tool Call Connection Error: {e}")

def test_sse():
    """Test SSE endpoint"""
    print("\n🌊 Testing SSE endpoint...")
    try:
        response = requests.get('http://localhost:8888/sse', 
                              headers={'Accept': 'text/event-stream'},
                              timeout=3, stream=True)
        
        print(f"✅ SSE Status: {response.status_code}")
        if response.status_code == 200:
            count = 0
            for line in response.iter_lines():
                if line and count < 3:  # Read first 3 lines
                    print(f"✅ SSE Data: {line.decode('utf-8')}")
                    count += 1
                elif count >= 3:
                    break
        else:
            print(f"❌ SSE Error: {response.text}")
            
    except Exception as e:
        print(f"❌ SSE Connection Error: {e}")

def test_sse_post():
    """Test SSE endpoint with POST"""
    print("\n📤 Testing SSE POST endpoint...")
    try:
        response = requests.post('http://localhost:8888/sse', 
                               json={'test': 'data', 'id': 'test123'},
                               headers={'Content-Type': 'application/json'},
                               timeout=5, stream=True)
        
        print(f"✅ SSE POST Status: {response.status_code}")
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    print(f"✅ SSE POST Data: {line.decode('utf-8')}")
                    break
        else:
            print(f"❌ SSE POST Error: {response.text}")
            
    except Exception as e:
        print(f"❌ SSE POST Connection Error: {e}")

if __name__ == "__main__":
    print("🚀 Testing HexStrike AI MCP Endpoints")
    print("=" * 50)
    
    test_http_mcp()
    test_sse()
    test_sse_post()
    
    print("\n" + "=" * 50)
    print("✨ Testing completed!")
