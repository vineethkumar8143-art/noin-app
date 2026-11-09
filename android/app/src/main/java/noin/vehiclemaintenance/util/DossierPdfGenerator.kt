package noin.vehiclemaintenance.util

import android.content.Context
import android.graphics.Color
import android.graphics.Paint
import android.graphics.pdf.PdfDocument
import noin.vehiclemaintenance.data.model.ServiceLog
import noin.vehiclemaintenance.data.model.Vehicle
import java.io.File
import java.io.FileOutputStream
import java.text.NumberFormat
import java.text.SimpleDateFormat
import java.util.*

object DossierPdfGenerator {

    /**
     * Generates a 100% on-device, zero-cost printable PDF Resale Dossier
     * using the Android SDK's built-in PdfDocument framework.
     */
    fun generateDossier(
        context: Context,
        vehicle: Vehicle,
        logs: List<ServiceLog>
    ): File {
        val pdfDocument = PdfDocument()
        val pageInfo = PdfDocument.PageInfo.Builder(595, 842, 1).create() // A4 standard (595 x 842 pt)
        val page = pdfDocument.startPage(pageInfo)
        val canvas = page.canvas

        val titlePaint = Paint().apply {
            color = Color.BLACK
            textSize = 20f
            isFakeBoldText = true
        }

        val subtitlePaint = Paint().apply {
            color = Color.DKGRAY
            textSize = 10f
        }

        val headerPaint = Paint().apply {
            color = Color.rgb(245, 158, 11) // Industrial Amber
            textSize = 11f
            isFakeBoldText = true
        }

        val textPaint = Paint().apply {
            color = Color.BLACK
            textSize = 10f
        }

        val mutedPaint = Paint().apply {
            color = Color.GRAY
            textSize = 9f
        }

        val borderPaint = Paint().apply {
            color = Color.LTGRAY
            strokeWidth = 1f
            style = Paint.Style.STROKE
        }

        var yPos = 50f

        // Document Header
        canvas.drawText("NOIN VEHICLE RESALE DOSSIER", 40f, yPos, titlePaint)
        yPos += 18f
        val dateFormatter = SimpleDateFormat("MMMM dd, yyyy", Locale.US)
        canvas.drawText("Generated on ${dateFormatter.format(Date())} • Verified Local Service History", 40f, yPos, subtitlePaint)
        yPos += 24f

        // Divider
        canvas.drawLine(40f, yPos, 555f, yPos, borderPaint)
        yPos += 20f

        // Vehicle Summary Box
        canvas.drawText("VEHICLE DETAILS", 40f, yPos, headerPaint)
        yPos += 16f
        canvas.drawText("Make & Model: ${vehicle.year} ${vehicle.make} ${vehicle.model}", 40f, yPos, textPaint)
        canvas.drawText("Current Odometer: ${NumberFormat.getNumberInstance(Locale.US).format(vehicle.currentOdometer)} ${vehicle.odometerUnit}", 300f, yPos, textPaint)
        yPos += 14f

        val vinString = vehicle.vin ?: "Not Recorded / Classic"
        canvas.drawText("VIN: $vinString", 40f, yPos, mutedPaint)
        
        val totalCostCents = logs.sumOf { it.costCents }
        val formattedCost = String.format(Locale.US, "%.2f", totalCostCents / 100.0)
        canvas.drawText("Documented Service Total: $${formattedCost}", 300f, yPos, mutedPaint)
        yPos += 25f

        // Table Header
        canvas.drawLine(40f, yPos, 555f, yPos, borderPaint)
        yPos += 16f
        canvas.drawText("DATE", 45f, yPos, headerPaint)
        canvas.drawText("ODOMETER", 130f, yPos, headerPaint)
        canvas.drawText("SERVICE RECORD & PARTS", 220f, yPos, headerPaint)
        canvas.drawText("COST", 490f, yPos, headerPaint)
        yPos += 8f
        canvas.drawLine(40f, yPos, 555f, yPos, borderPaint)
        yPos += 18f

        // Table Rows
        val rowDateFormat = SimpleDateFormat("yyyy-MM-dd", Locale.US)
        for (log in logs.take(25)) { // First 25 records on page 1
            canvas.drawText(rowDateFormat.format(Date(log.serviceDate)), 45f, yPos, textPaint)
            canvas.drawText("${NumberFormat.getNumberInstance(Locale.US).format(log.odometer)} ${vehicle.odometerUnit}", 130f, yPos, textPaint)
            
            val displayTitle = if (log.title.length > 36) log.title.take(33) + "..." else log.title
            canvas.drawText(displayTitle, 220f, yPos, textPaint)
            
            val itemCost = String.format(Locale.US, "$%.2f", log.costCents / 100.0)
            canvas.drawText(itemCost, 490f, yPos, textPaint)
            
            yPos += 14f
            if (!log.partNumbers.isNullOrBlank()) {
                canvas.drawText("Parts: ${log.partNumbers}", 220f, yPos, mutedPaint)
                yPos += 12f
            }
            yPos += 4f
        }

        // Footer Guarantee
        canvas.drawLine(40f, 790f, 555f, 790f, borderPaint)
        canvas.drawText("Noin Local-First Guarantee: Unaltered, user-maintained maintenance ledger.", 40f, 808f, mutedPaint)

        pdfDocument.finishPage(page)

        // Save to cache directory
        val cacheDir = File(context.cacheDir, "dossiers").apply { mkdirs() }
        val pdfFile = File(cacheDir, "${vehicle.make}_${vehicle.model}_Dossier.pdf")
        val outputStream = FileOutputStream(pdfFile)
        pdfDocument.writeTo(outputStream)
        outputStream.close()
        pdfDocument.close()

        return pdfFile
    }
}
