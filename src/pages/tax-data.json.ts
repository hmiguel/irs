import taxData from '../data/tax-data.json';

export async function GET() {
  return new Response(JSON.stringify(taxData), {
    headers: { 'Content-Type': 'application/json' },
  });
}
