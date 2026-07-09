import { readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";

const root = process.cwd();

export type SiteConfig = {
  name: string;
  tagline: string;
  subtitle: string;
  phone: string;
  phoneTel: string;
  address: {
    line1: string;
    line2: string;
    postcode: string;
    full: string;
  };
  mapsUrl: string;
  mapsEmbed: string;
  facebook: string;
  facebookLabel: string;
  justEat: boolean;
  justEatUrl: string;
  justEatLabel: string;
  hero: {
    title: string;
    text: string;
    ctaMenu: string;
    ctaCall: string;
    image: string;
    imageNote: string;
  };
  about: {
    heading: string;
    text: string;
  };
  seo: {
    title: string;
    description: string;
  };
  footer: {
    note: string;
  };
};

export type MenuItem = {
  id: string;
  name: string;
  description: string;
  price: string;
  image: string;
};

export type MenuExtra = {
  name: string;
  price: string;
};

export type MenuCategory = {
  id: string;
  name: string;
  blurb?: string;
  items: MenuItem[];
  extras?: MenuExtra[];
  notes?: string[];
};

function readJson<T>(path: string): T {
  return JSON.parse(readFileSync(path, "utf-8")) as T;
}

export function getSite(): SiteConfig {
  return readJson<SiteConfig>(join(root, "content", "site.json"));
}

export function getMenuCategories(): MenuCategory[] {
  const index = readJson<{ order: string[] }>(
    join(root, "content", "menu", "index.json"),
  );
  const dir = join(root, "content", "menu");
  const files = readdirSync(dir).filter(
    (f) => f.endsWith(".json") && f !== "index.json",
  );

  const byId = new Map<string, MenuCategory>();
  for (const file of files) {
    const cat = readJson<MenuCategory>(join(dir, file));
    byId.set(cat.id, cat);
  }

  return index.order
    .map((id) => byId.get(id))
    .filter((c): c is MenuCategory => Boolean(c));
}
