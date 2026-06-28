# Currency exchange rates (base: EUR)
EXCHANGE_RATES = {
    "EUR": 1.0,      # Base currency
    "USD": 1.10,     # 1 EUR = 1.10 USD (approximate)
    "CAD": 1.50,     # 1 EUR = 1.50 CAD (approximate)
}

CURRENCY_SYMBOLS = {
    "EUR": "€",
    "USD": "$",
    "CAD": "CAD $",
}

CURRENCY_NAMES = {
    "EUR": "Euro",
    "USD": "US Dollar",
    "CAD": "Canadian Dollar",
}

# Game requirements database (40+ games)
GAME_PROFILES = {
    # Esports / Competitive (Low tier)
    "valorant": {"tier": "low", "vram_min": 2},
    "cs2": {"tier": "low", "vram_min": 2},
    "cs:go": {"tier": "low", "vram_min": 2},
    "league of legends": {"tier": "low", "vram_min": 2},
    "dota 2": {"tier": "low", "vram_min": 2},
    "overwatch 2": {"tier": "low", "vram_min": 3},
    "apex legends": {"tier": "low", "vram_min": 3},
    "fortnite": {"tier": "medium", "vram_min": 4},
    
    # Casual / Indie (Low to Medium)
    "roblox": {"tier": "low", "vram_min": 2},
    "minecraft": {"tier": "low", "vram_min": 2},
    "stardew valley": {"tier": "low", "vram_min": 1},
    "terraria": {"tier": "low", "vram_min": 1},
    "among us": {"tier": "low", "vram_min": 1},
    "elden ring": {"tier": "medium", "vram_min": 8},
    "palworld": {"tier": "medium", "vram_min": 4},
    "helldivers 2": {"tier": "medium", "vram_min": 4},
    "valheim": {"tier": "low", "vram_min": 2},
    "hades": {"tier": "low", "vram_min": 2},
    
    # AAA Open-World (Medium)
    "gtav": {"tier": "medium", "vram_min": 3},
    "gta v": {"tier": "medium", "vram_min": 3},
    "red dead redemption 2": {"tier": "medium", "vram_min": 6},
    "red dead 2": {"tier": "medium", "vram_min": 6},
    "skyrim": {"tier": "medium", "vram_min": 2},
    "the witcher 3": {"tier": "medium", "vram_min": 4},
    "witcher 3": {"tier": "medium", "vram_min": 4},
    "starfield": {"tier": "high", "vram_min": 8},
    "fallout 4": {"tier": "medium", "vram_min": 3},
    
    # Demanding AAA (High tier)
    "cyberpunk 2077": {"tier": "high", "vram_min": 8},
    "cyberpunk": {"tier": "high", "vram_min": 8},
    "baldurs gate 3": {"tier": "high", "vram_min": 8},
    "baldur's gate 3": {"tier": "high", "vram_min": 8},
    "alan wake 2": {"tier": "high", "vram_min": 8},
    "star wars outlaws": {"tier": "high", "vram_min": 8},
    "dragon's dogma 2": {"tier": "high", "vram_min": 8},
    "final fantasy xvi": {"tier": "high", "vram_min": 8},
    
    # Competitive FPS (Medium to High)
    "call of duty": {"tier": "medium", "vram_min": 4},
    "call of duty mw3": {"tier": "medium", "vram_min": 6},
    "call of duty modern warfare": {"tier": "medium", "vram_min": 6},
    "counter-strike 2": {"tier": "low", "vram_min": 2},
    "rainbow six siege": {"tier": "medium", "vram_min": 4},
    "destiny 2": {"tier": "medium", "vram_min": 4},
    "warframe": {"tier": "medium", "vram_min": 4},
}

# PC Components with prices in EUR
PRODUCTS = {
    "CPU": {
        "low": [
            {"name": "Intel Core i3-13100F", "price_eur": 120, "specs": "4-core / 8-thread, 3.4-4.1 GHz", "affiliate_url": "https://amazon.de/s?k=Core+i3-13100F&tag=YOUR_AFFILIATE"},
            {"name": "AMD Ryzen 3 4100", "price_eur": 105, "specs": "4-core / 4-thread, 3.8-4.2 GHz", "affiliate_url": "https://amazon.de/s?k=Ryzen+3+4100&tag=YOUR_AFFILIATE"},
            {"name": "Intel Core i5-12400F", "price_eur": 180, "specs": "6-core / 12-thread, 3.3-4.4 GHz", "affiliate_url": "https://amazon.de/s?k=Core+i5-12400F&tag=YOUR_AFFILIATE"}
        ],
        "medium": [
            {"name": "AMD Ryzen 5 5600", "price_eur": 210, "specs": "6-core / 12-thread, 3.5-4.6 GHz", "affiliate_url": "https://amazon.de/s?k=Ryzen+5+5600&tag=YOUR_AFFILIATE"},
            {"name": "Intel Core i5-13600K", "price_eur": 280, "specs": "14-core / 20-thread, 3.5-5.1 GHz", "affiliate_url": "https://amazon.de/s?k=Core+i5-13600K&tag=YOUR_AFFILIATE"},
            {"name": "AMD Ryzen 5 7600X", "price_eur": 250, "specs": "6-core / 12-thread, 4.7-5.6 GHz", "affiliate_url": "https://amazon.de/s?k=Ryzen+5+7600X&tag=YOUR_AFFILIATE"}
        ],
        "high": [
            {"name": "AMD Ryzen 7 7800X3D", "price_eur": 420, "specs": "8-core / 16-thread, 4.2-5.0 GHz, 3D V-Cache", "affiliate_url": "https://amazon.de/s?k=Ryzen+7+7800X3D&tag=YOUR_AFFILIATE"},
            {"name": "Intel Core i9-13900K", "price_eur": 590, "specs": "24-core / 32-thread, 3.0-5.8 GHz", "affiliate_url": "https://amazon.de/s?k=Core+i9-13900K&tag=YOUR_AFFILIATE"},
            {"name": "AMD Ryzen 9 7950X", "price_eur": 550, "specs": "16-core / 32-thread, 4.5-5.7 GHz", "affiliate_url": "https://amazon.de/s?k=Ryzen+9+7950X&tag=YOUR_AFFILIATE"}
        ]
    },
    
    "GPU": {
        "low": [
            {"name": "NVIDIA GeForce GTX 1650", "price_eur": 180, "vram": "4GB GDDR6", "specs": "1410 MHz, 896 CUDA cores", "affiliate_url": "https://amazon.de/s?k=GTX+1650&tag=YOUR_AFFILIATE"},
            {"name": "AMD Radeon RX 6500 XT", "price_eur": 160, "vram": "4GB GDDR6", "specs": "2685 MHz, 1024 Stream Processors", "affiliate_url": "https://amazon.de/s?k=RX+6500+XT&tag=YOUR_AFFILIATE"},
            {"name": "Intel Arc A770", "price_eur": 190, "vram": "4GB GDDR6", "specs": "2400 MHz, 32 Xe-Cores", "affiliate_url": "https://amazon.de/s?k=Arc+A770&tag=YOUR_AFFILIATE"}
        ],
        "medium": [
            {"name": "NVIDIA GeForce RTX 4060", "price_eur": 290, "vram": "8GB GDDR6", "specs": "2505 MHz, 3072 CUDA cores", "affiliate_url": "https://amazon.de/s?k=RTX+4060&tag=YOUR_AFFILIATE"},
            {"name": "AMD Radeon RX 6700 XT", "price_eur": 340, "vram": "12GB GDDR6", "specs": "2655 MHz, 2560 Stream Processors", "affiliate_url": "https://amazon.de/s?k=RX+6700+XT&tag=YOUR_AFFILIATE"},
            {"name": "NVIDIA GeForce RTX 4060 Ti", "price_eur": 410, "vram": "8GB GDDR6", "specs": "2535 MHz, 4352 CUDA cores", "affiliate_url": "https://amazon.de/s?k=RTX+4060+Ti&tag=YOUR_AFFILIATE"}
        ],
        "high": [
            {"name": "NVIDIA GeForce RTX 4070 Super", "price_eur": 580, "vram": "12GB GDDR6X", "specs": "2610 MHz, 5888 CUDA cores", "affiliate_url": "https://amazon.de/s?k=RTX+4070+Super&tag=YOUR_AFFILIATE"},
            {"name": "NVIDIA GeForce RTX 4080 Super", "price_eur": 900, "vram": "16GB GDDR6X", "specs": "2505 MHz, 10240 CUDA cores", "affiliate_url": "https://amazon.de/s?k=RTX+4080+Super&tag=YOUR_AFFILIATE"},
            {"name": "NVIDIA GeForce RTX 4090", "price_eur": 1600, "vram": "24GB GDDR6X", "specs": "2520 MHz, 16384 CUDA cores", "affiliate_url": "https://amazon.de/s?k=RTX+4090&tag=YOUR_AFFILIATE"}
        ]
    },
    
    "RAM": {
        "low": [
            {"name": "Corsair Vengeance LPX 16GB", "price_eur": 55, "specs": "DDR4-3200 MHz, CAS 16", "affiliate_url": "https://amazon.de/s?k=Corsair+Vengeance+LPX+16GB&tag=YOUR_AFFILIATE"},
            {"name": "Kingston Fury Beast 16GB", "price_eur": 50, "specs": "DDR4-3200 MHz, CAS 16", "affiliate_url": "https://amazon.de/s?k=Kingston+Fury+Beast+16GB&tag=YOUR_AFFILIATE"},
            {"name": "G.Skill Flare X5 16GB", "price_eur": 65, "specs": "DDR5-6000 MHz, CAS 30", "affiliate_url": "https://amazon.de/s?k=G.Skill+Flare+X5+16GB&tag=YOUR_AFFILIATE"}
        ],
        "medium": [
            {"name": "Corsair Vengeance RGB Pro 32GB", "price_eur": 120, "specs": "DDR5-5600 MHz, CAS 28, RGB", "affiliate_url": "https://amazon.de/s?k=Corsair+Vengeance+RGB+Pro+32GB&tag=YOUR_AFFILIATE"},
            {"name": "G.Skill Trident Z5 32GB", "price_eur": 140, "specs": "DDR5-6000 MHz, CAS 30", "affiliate_url": "https://amazon.de/s?k=G.Skill+Trident+Z5+32GB&tag=YOUR_AFFILIATE"},
            {"name": "Kingston Fury Renegade 32GB", "price_eur": 130, "specs": "DDR5-6400 MHz, CAS 32", "affiliate_url": "https://amazon.de/s?k=Kingston+Fury+Renegade+32GB&tag=YOUR_AFFILIATE"}
        ],
        "high": [
            {"name": "Corsair Dominator Platinum RGB 64GB", "price_eur": 340, "specs": "DDR5-6000 MHz, CAS 30, RGB, Dual Channel", "affiliate_url": "https://amazon.de/s?k=Corsair+Dominator+Platinum+64GB&tag=YOUR_AFFILIATE"},
            {"name": "G.Skill Trident Z5 RGB 64GB", "price_eur": 360, "specs": "DDR5-6000 MHz, CAS 30, RGB", "affiliate_url": "https://amazon.de/s?k=G.Skill+Trident+Z5+RGB+64GB&tag=YOUR_AFFILIATE"},
            {"name": "Kingston HyperX Predator 64GB", "price_eur": 350, "specs": "DDR5-5600 MHz, CAS 28", "affiliate_url": "https://amazon.de/s?k=Kingston+HyperX+Predator+64GB&tag=YOUR_AFFILIATE"}
        ]
    },
    
    "Storage": {
        "low": [
            {"name": "Kingston A2000 500GB NVMe", "price_eur": 35, "specs": "NVMe SSD, PCIe 3.0, 2000MB/s Read", "affiliate_url": "https://amazon.de/s?k=Kingston+A2000+500GB&tag=YOUR_AFFILIATE"},
            {"name": "Western Digital SN850X 500GB", "price_eur": 40, "specs": "NVMe SSD, PCIe 4.0, 7100MB/s Read", "affiliate_url": "https://amazon.de/s?k=WD+SN850X+500GB&tag=YOUR_AFFILIATE"},
            {"name": "Samsung 870 EVO 500GB SSD", "price_eur": 38, "specs": "SATA SSD, 560MB/s Read", "affiliate_url": "https://amazon.de/s?k=Samsung+870+EVO+500GB&tag=YOUR_AFFILIATE"}
        ],
        "medium": [
            {"name": "Samsung 990 Pro 1TB NVMe", "price_eur": 110, "specs": "NVMe SSD, PCIe 4.0, 7100MB/s Read, Heat Sink", "affiliate_url": "https://amazon.de/s?k=Samsung+990+Pro+1TB&tag=YOUR_AFFILIATE"},
            {"name": "Crucial P5 Plus 1TB NVMe", "price_eur": 95, "specs": "NVMe SSD, PCIe 4.0, 6600MB/s Read", "affiliate_url": "https://amazon.de/s?k=Crucial+P5+Plus+1TB&tag=YOUR_AFFILIATE"},
            {"name": "Samsung 870 EVO 1TB SSD", "price_eur": 75, "specs": "SATA SSD, 560MB/s Read, Durable", "affiliate_url": "https://amazon.de/s?k=Samsung+870+EVO+1TB&tag=YOUR_AFFILIATE"}
        ],
        "high": [
            {"name": "Samsung 990 Pro 4TB NVMe", "price_eur": 380, "specs": "NVMe SSD, PCIe 4.0, 7100MB/s Read, Heat Sink", "affiliate_url": "https://amazon.de/s?k=Samsung+990+Pro+4TB&tag=YOUR_AFFILIATE"},
            {"name": "Western Digital Black SN850X 2TB", "price_eur": 220, "specs": "NVMe SSD, PCIe 4.0, 7100MB/s Read, High Speed", "affiliate_url": "https://amazon.de/s?k=WD+Black+SN850X+2TB&tag=YOUR_AFFILIATE"},
            {"name": "Crucial T700 2TB NVMe", "price_eur": 240, "specs": "NVMe SSD, PCIe 5.0, 12400MB/s Read", "affiliate_url": "https://amazon.de/s?k=Crucial+T700+2TB&tag=YOUR_AFFILIATE"}
        ]
    },
    
    "PSU": {
        "low": [
            {"name": "Thermaltake Smart BM2 550W", "price_eur": 50, "specs": "550W, 80+ Bronze, Non-Modular", "affiliate_url": "https://amazon.de/s?k=Thermaltake+Smart+BM2+550W&tag=YOUR_AFFILIATE"},
            {"name": "MSI MAG A550BN 550W", "price_eur": 58, "specs": "550W, 80+ Bronze, Semi-Modular", "affiliate_url": "https://amazon.de/s?k=MSI+MAG+A550BN&tag=YOUR_AFFILIATE"},
            {"name": "Corsair CV550 550W", "price_eur": 55, "specs": "550W, 80+ Bronze, Non-Modular", "affiliate_url": "https://amazon.de/s?k=Corsair+CV550&tag=YOUR_AFFILIATE"}
        ],
        "medium": [
            {"name": "Corsair RM750e 750W", "price_eur": 95, "specs": "750W, 80+ Gold, Fully Modular, 10 Year Warranty", "affiliate_url": "https://amazon.de/s?k=Corsair+RM750e&tag=YOUR_AFFILIATE"},
            {"name": "EVGA SuperNOVA 750W Gold", "price_eur": 90, "specs": "750W, 80+ Gold, Semi-Modular, ECO Mode", "affiliate_url": "https://amazon.de/s?k=EVGA+SuperNOVA+750W&tag=YOUR_AFFILIATE"},
            {"name": "Seasonic Focus Gold 650W", "price_eur": 85, "specs": "650W, 80+ Gold, Fully Modular, Fanless Mode", "affiliate_url": "https://amazon.de/s?k=Seasonic+Focus+Gold+650W&tag=YOUR_AFFILIATE"}
        ],
        "high": [
            {"name": "Corsair RM1000e 1000W", "price_eur": 170, "specs": "1000W, 80+ Gold, Fully Modular, Quiet, 10 Year Warranty", "affiliate_url": "https://amazon.de/s?k=Corsair+RM1000e&tag=YOUR_AFFILIATE"},
            {"name": "EVGA SuperNOVA 1000W Platinum", "price_eur": 180, "specs": "1000W, 80+ Platinum, Fully Modular, Eco Mode", "affiliate_url": "https://amazon.de/s?k=EVGA+SuperNOVA+1000W+Platinum&tag=YOUR_AFFILIATE"},
            {"name": "Seasonic Prime Titanium 850W", "price_eur": 200, "specs": "850W, 80+ Titanium, Fully Modular, Ultra Efficient", "affiliate_url": "https://amazon.de/s?k=Seasonic+Prime+Titanium+850W&tag=YOUR_AFFILIATE"}
        ]
    },
    
    "Motherboard": {
        "low": [
            {"name": "MSI PRO B650M-A WiFi", "price_eur": 130, "specs": "AM5 Socket, Micro-ATX, PCIe 5.0, WiFi 6E", "affiliate_url": "https://amazon.de/s?k=MSI+PRO+B650M-A&tag=YOUR_AFFILIATE"},
            {"name": "ASUS TUF B650M-E", "price_eur": 150, "specs": "AM5 Socket, Micro-ATX, Durable, PCIe 5.0", "affiliate_url": "https://amazon.de/s?k=ASUS+TUF+B650M-E&tag=YOUR_AFFILIATE"},
            {"name": "Gigabyte B650E Aorus Master", "price_eur": 180, "specs": "AM5 Socket, ATX, PCIe 5.0, 16 Power Phases", "affiliate_url": "https://amazon.de/s?k=Gigabyte+B650E+Aorus&tag=YOUR_AFFILIATE"}
        ],
        "medium": [
            {"name": "MSI MPG B850E EDGE WIFI", "price_eur": 280, "specs": "AM5 Socket, ATX, PCIe 5.0, WiFi 7, Premium Features", "affiliate_url": "https://amazon.de/s?k=MSI+MPG+B850E+EDGE&tag=YOUR_AFFILIATE"},
            {"name": "ASUS ROG X870-E HERO", "price_eur": 320, "specs": "AM5 Socket, ATX, PCIe 5.0, WiFi 6E, Premium VRM", "affiliate_url": "https://amazon.de/s?k=ASUS+ROG+X870-E+HERO&tag=YOUR_AFFILIATE"},
            {"name": "Gigabyte X870E AORUS Master", "price_eur": 300, "specs": "AM5 Socket, ATX, PCIe 5.0, 26 Power Phases, ECC Memory", "affiliate_url": "https://amazon.de/s?k=Gigabyte+X870E+Aorus+Master&tag=YOUR_AFFILIATE"}
        ],
        "high": [
            {"name": "ASUS ROG MAXIMUS Z890-E HERO", "price_eur": 450, "specs": "LGA1700 Socket, ATX, PCIe 5.0, WiFi 7, Overclocking Ready", "affiliate_url": "https://amazon.de/s?k=ASUS+ROG+Z890&tag=YOUR_AFFILIATE"},
            {"name": "MSI MPG Z890 ACE", "price_eur": 480, "specs": "LGA1700 Socket, ATX, PCIe 5.0, WiFi 7, Premium Audio", "affiliate_url": "https://amazon.de/s?k=MSI+MPG+Z890+ACE&tag=YOUR_AFFILIATE"},
            {"name": "Gigabyte Z890 AORUS MASTER", "price_eur": 500, "specs": "LGA1700 Socket, ATX, PCIe 5.0, WiFi 7, 28 Power Phases", "affiliate_url": "https://amazon.de/s?k=Gigabyte+Z890+Aorus&tag=YOUR_AFFILIATE"}
        ]
    }
}

def convert_price(price_eur, currency):
    """Convert price from EUR to target currency"""
    if currency not in EXCHANGE_RATES:
        currency = "EUR"
    rate = EXCHANGE_RATES[currency]
    return round(price_eur * rate, 2)

def get_build_recommendation(budget, games, currency="EUR"):
    """
    Generate PC build recommendation based on games and budget
    
    Args:
        budget (int): Total budget in chosen currency
        games (list): List of game names (lowercase)
        currency (str): Currency code (EUR, USD, CAD)
    
    Returns:
        dict: Build recommendation with components and prices
    """
    
    # Convert budget to EUR for internal calculations
    budget_eur = budget / EXCHANGE_RATES.get(currency, 1.0)
    
    # Determine tier based on games played
    tier = "medium"  # Default tier
    max_game_tier = "low"
    
    # Find the most demanding game in the list
    for game in games:
        if game in GAME_PROFILES:
            game_tier = GAME_PROFILES[game]["tier"]
            if game_tier == "high":
                max_game_tier = "high"
            elif game_tier == "medium" and max_game_tier == "low":
                max_game_tier = "medium"
    
    # Adjust tier based on budget constraints
    if budget_eur < 700:
        tier = "low"
    elif budget_eur < 1500:
        tier = "medium"
    else:
        tier = "high"
    
    # Games should override budget downward
    if max_game_tier == "high":
        tier = "high"
    elif max_game_tier == "medium" and tier == "low":
        tier = "medium"
    
    # Build recommendation
    build = {
        "tier": tier.upper(),
        "currency": currency,
        "currency_symbol": CURRENCY_SYMBOLS[currency],
        "estimated_total_eur": 0,
        "estimated_total": 0,
        "components": {},
        "budget": budget,
    }
    
    # Select products for each component category
    for component, tiers_dict in PRODUCTS.items():
        if tier in tiers_dict and tiers_dict[tier]:
            product = tiers_dict[tier][0]
            
            component_data = {
                "name": product["name"],
                "price_eur": product["price_eur"],
                "price": convert_price(product["price_eur"], currency),
                "affiliate_url": product["affiliate_url"],
            }
            
            if "specs" in product:
                component_data["details"] = product["specs"]
            elif "vram" in product:
                component_data["details"] = product["vram"]
            
            build["components"][component] = component_data
            build["estimated_total_eur"] += product["price_eur"]
    
    # Convert total to target currency
    build["estimated_total"] = convert_price(build["estimated_total_eur"], currency)
    
    # Determine if build fits budget
    build["fits_budget"] = build["estimated_total"] <= budget
    build["budget_remaining"] = budget - build["estimated_total"]
    
    return build

def get_all_games():
    """Return list of all available games"""
    return sorted(list(GAME_PROFILES.keys()))

def get_game_info(game_name):
    """Get tier and requirements for a specific game"""
    return GAME_PROFILES.get(game_name.lower())
