# Spammies Sandwich Shop

Modern static website for **Spammies**, a family-owned sandwich shop in Morley, Leeds.

- **Stack:** Astro + Tailwind CSS  
- **Host:** Vercel-ready (`npm run build` → static `dist/`)  
- **Content:** editable JSON under `content/`  
- **Images:** `public/images/`

## Quick start

```bash
cd spammies-website
npm install
npm run dev
```

Open [http://localhost:4321](http://localhost:4321).

```bash
npm run build    # production build → dist/
npm run preview  # preview production build
```

## Edit site details (phone, address, copy)

Edit **`content/site.json`**:

- `phone` / `phoneTel`  -  display number and `tel:` link  
- `address`  -  line1, line2, postcode, full  
- `mapsUrl` / `mapsEmbed`  -  Google Maps links  
- `hero`, `about`, `seo`, `footer`  -  page text  

No code changes needed.

## Edit the menu

1. Open the right category file in **`content/menu/`**:

   | File | Section |
   |------|---------|
   | `breakfasts.json` | All-day breakfasts |
   | `hot-sandwiches.json` | Hot sandwiches |
   | `cold-sandwiches.json` | Cold sandwiches |
   | `toasties.json` | Grilled toasties |
   | `omelettes.json` | Omelettes |
   | `jackets.json` | Jacket potatoes |
   | `burgers.json` | Burgers |
   | `salads.json` | Salad boxes |
   | `others.json` | Others (toast, chips, cakes…) |
   | `drinks.json` | Drinks |

2. **Add an item**  -  copy an existing object in `items` and change fields:

```json
{
  "id": "my-new-item",
  "name": "My New Item",
  "description": "Short description for the card.",
  "price": "3.50",
  "image": "/images/menu/my-new-item.jpg"
}
```

3. **Remove an item**  -  delete that object from `items`.  
4. **Reorder categories**  -  edit `content/menu/index.json` (`order` array).  
5. **Extras / notes**  -  optional `extras` and `notes` arrays on a category.

Prices are shown with a £ prefix automatically (store numbers only, e.g. `"3.50"`).

## Replace images

| Path | Purpose |
|------|---------|
| `public/images/brand/sign.jpg` | Shop sign on the home page |
| `public/images/hero/hero-placeholder.jpg` | Hero background  -  replace with a real shop photo |
| `public/images/menu/*.jpg` | Menu item photos (filename must match the `image` path in JSON) |

Recommended: JPG or WebP, roughly 1200×900 for menu cards, 1920×1080 for hero.

## Brand colours (from the shop sign)

- Navy: `#1B3A4B`  
- Gold: `#E8C84A`  
- Cream: `#F3EBD4`  

Defined in `src/styles/global.css` (`@theme`).

## Deploy on Vercel

1. Push this folder to GitHub.  
2. Import the repo in [Vercel](https://vercel.com).  
3. Framework: **Astro** (auto-detected).  
4. Build command: `npm run build`  
5. Output: `dist`

Or CLI:

```bash
npx vercel
```

## Project structure

```
content/           # site + menu JSON (edit these)
public/images/     # brand, hero, menu images
src/
  components/      # Nav, Footer, MenuCard, …
  layouts/         # BaseLayout
  lib/content.ts   # loaders for JSON
  pages/           # index (home), menu
  styles/          # Tailwind + brand tokens
```

## Contact (seeded from the shop)

- **Address:** Spammies, 135 Wide Lane, Morley, Leeds LS27 8DF  
- **Phone:** 07902 771 542  
