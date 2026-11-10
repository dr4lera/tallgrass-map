# Map

A coarse biome-only Overworld map: https://dr4lera.github.io/tallgrass-map/

Drag to pan, scroll or use +/− to zoom, and select a biome to highlight it. The home button resets the view. Keyboard navigation supports arrow keys, +/− and Home.

## Data

This is a dated snapshot of generated server terrain, aggregated into 64×64-block cells. Each cell shows the most sampled surface biome, so small biomes and precise boundaries are intentionally omitted. Dark areas have no exported data.

The published JSON contains only biome identifiers, coarse cell coordinates, and a snapshot timestamp. It contains no world seed, structures, blocks, heightmaps, player data, claims, or entities. Raw world files must never be uploaded here.

## Updating

Replace `biomes.json` with a fresh sanitized export, keeping the same schema, and commit to `main`. GitHub Pages publishes from the repository root. The server addon exports newly loaded/generated Overworld chunks once a minute. A GitHub Actions job syncs the sanitized JSON approximately every five minutes (scheduling can be delayed), and open pages check once a minute. No player positions are tracked. The first live update requires restarting into the staged server addon.

No server restart or extra client mod is required.
