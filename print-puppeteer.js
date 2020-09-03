// node print-puppeteer.js --html "tmp_out_facture.html" --css "templates/devis.css" --pdf out_puppeteer.pdf --header "Facture n° 20200801"
// node -v -> v14.1.0

const puppeteer = require('puppeteer');
const fs = require('fs-extra');

// Faire que le script retourne les données du fichiers au lieu de l'écrire sur le disque ?
// https://2ality.com/2011/12/nodejs-shell-scripting.html
// Arguments du script
// https://www.digitalocean.com/community/tutorials/nodejs-command-line-arguments-node-scripts
const commander = require('commander');

commander
  .option('--html <html>')
  .option('--css <css>')
  .option('--pdf <pdf>')
  .option('--header <header>')
  .parse(process.argv);
  
const htmlPath = commander.html;
const cssPath = commander.css;
const pdfPath = commander.pdf;
const headerContent = commander.header;

(async function printPDF() {
  try {
    const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox'], executablePath: "/snap/bin/chromium", headless: true});
    const page = await browser.newPage();
    const html = await fs.readFile(htmlPath, 'utf-8')
    await page.setContent(html)
    await page.addStyleTag({path: cssPath})
    const pdf = await page.pdf({ 
      // path: pdfPath,
      format: 'A4',
      displayHeaderFooter: true,
      headerTemplate: `<style>#pageHeader { margin: 20px; }</style><div class="text" id="pageHeader">${headerContent}</div>`,
      footerTemplate: '<div class="text center"><span class="pageNumber"></span></div>',
    });
   
    console.log(pdf.toString())
    await browser.close();
  } catch (e) {
    // console.log('Erreur:',e);
  }
})();