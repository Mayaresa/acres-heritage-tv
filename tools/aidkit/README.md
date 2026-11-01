# AID channel kit

Each AID (distributor) gets a personal TV link: `https://mayaresa.github.io/acres-heritage-tv/?aid=<slug>`.
Orders from that link go to the AID's WhatsApp; the order area shows a sea-blue "Your Local FONIO Distributor" box.

## Add an AID
1. Add an entry to `/aids.json` (repo root):
```json
"slug": {"name": "Full Name", "role": "AID", "area": "Madina", "zone": "Madina – Adenta", "wa": "233541234567", "active": true}
```
- `wa`: digits only, with country code (Ghana 233…, US 1…).
- `area` shows as "<area> & Surroundings". `zone` should contain a zone word from the order form (e.g. Kaneshie, Madina) so it is pre-selected.
- Diaspora AIDs: add `"label": "Your Diaspora FONIO Distributor", "areaText": "Send fonio to family in Ghana", "gift": true` (adds recipient name/phone to the order form).
- To switch an AID off: `"active": false`.
2. Commit and push to `main` (GitHub Pages republishes in ~1 minute).
3. Send the AID their link + welcome message (WhatsApp). No QR sign needed (decided Nov 2026).
   Optional, only if asked: `python3 tools/aidkit/make_kit.py <slug>` makes a printable QR sign.
