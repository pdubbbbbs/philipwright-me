#!/bin/bash
echo "🌐 Verifying philipwright.me DNS Configuration"
echo "=" * 50

echo "📡 DNS A Records:"
dig +short philipwright.me A

echo "📡 DNS CNAME for www:"
dig +short www.philipwright.me

echo "🔍 Testing HTTP connectivity:"
curl -I -s -o /dev/null -w "HTTP Status: %{http_code}\n" https://philipwright.me 2>/dev/null || echo "Domain not accessible yet"

echo "🕐 Note: DNS propagation can take 2-60 minutes"
echo "✅ Expected A record IPs: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153"
