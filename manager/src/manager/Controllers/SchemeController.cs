using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using System.Net.Http;
using System.Net.Http.Headers;

// For more information on enabling MVC for empty projects, visit http://go.microsoft.com/fwlink/?LinkID=397860

namespace manager.Controllers
{
    public class SchemeController : Controller
    {
        private string Host = Environment.GetEnvironmentVariable("AirhornDB_URL");

        // GET: /<controller>/
        public async Task<IActionResult> Index()
        {
            // Get the current scheme from the database
            var httpClient = new HttpClient();
            httpClient.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue("Airhorn", "1.0"));
            string url = String.Format("{0}/{1}/{2}", Host, "schemes", "GUID");
            var result = await httpClient.GetStringAsync(url);

            return View(result);
        }
    }
}
