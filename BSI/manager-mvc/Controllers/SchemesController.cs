using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using System.IO;
using manager_mvc.Models;
using System.Net.Http;
using System.Net.Http.Headers;
using Newtonsoft.Json;

// For more information on enabling MVC for empty projects, visit http://go.microsoft.com/fwlink/?LinkID=397860

namespace manager_mvc.Controllers
{
    public class SchemesController : Controller
    {
        private string Host = Environment.GetEnvironmentVariable("AirhornDB_URL");

        // GET: /<controller>/
        public async Task<IActionResult> Index()
        {
            // Get all local sound schemes and list them
            // Indicate the current scheme 
            SchemeList lstSchemes = new SchemeList();
            lstSchemes = await List();
            return View(lstSchemes);
        }

        //public async Task Load(Guid id)
        //{
        //    var httpClient = new HttpClient();
        //    httpClient.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue("MyClient", "1.0"));
        //    // Get the json string
        //    var result = await httpClient.GetStringAsync(String.Format("{0}/schemes/{1}", Host, id));
        //    // Parse it into a Scheme Object
        //    SoundScheme s = (SoundScheme)JsonConvert.DeserializeObject(result);
        //    this.isCurrentScheme = s.isCurrentScheme;
        //    this.SchemeId = s.SchemeId;
        //    this.Name = s.Name;
        //}

        public async Task<SchemeList> List()
        {
            using (var httpClient = new HttpClient())
            {
                httpClient.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue("MyClient", "1.0"));
                // Get the json string
                var result = await httpClient.GetStringAsync(String.Format("{0}/schemes", Host));
                // Parse it into a List of Scheme Objects
                List<Scheme> s = JsonConvert.DeserializeObject<List<Scheme>>(result);
                SchemeList lstSchemes = new SchemeList();
                lstSchemes.lstSchemes = s;
                // Load each scheme's sound metadata
                foreach (Scheme scheme in s)
                {
                    string url = String.Format("{0}/scheme-sounds?SchemeId={1}", Host, scheme.Id);
                    var ss = await httpClient.GetStringAsync(url);
                    List<Scheme_Sound> lstSS = JsonConvert.DeserializeObject<List<Scheme_Sound>>(ss);
                    scheme.Sounds = lstSS;
                }
                return lstSchemes;
            }
        }
    }
}
